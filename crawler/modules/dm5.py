#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import execjs
from crawler.utils import get_content, do_request, default
from urllib.parse import urljoin, urlsplit
from os.path import split

domain = "www.dm5.com"


def get_comic(url):
    content = get_content(url)
    pattern = re.compile(r"<a class=\"tg\" href=\"(.*?)\" title=\"(.*?)\"", re.S)
    chapters = pattern.findall(content)
    return {urljoin(url, c[0]): c[1] for c in chapters}


def get_chapter(referer, url):
    header = default
    header["Referer"] = referer
    header["Host"] = domain
    content = get_content(url, header)
    count = re.search(r"DM5_IMAGE_COUNT=(\d+)", content).group(1)
    cid = re.search(r"DM5_CID=(\d+)", content).group(1)
    key, gtk, language = "", "6", "1"

    images = []
    for page in range(1, int(count) + 1):
        i_url = "{0}chapterfun.ashx?cid={1}&page={2}&key={3}&language={4}&gtk={5}".format(url, cid, page, key,
                                                                                          language, gtk)
        header["Referer"] = url
        header["X-Requested-With"] = "XMLHttpRequest"
        js = get_content(i_url, header)
        images.extend(execjs.eval(js))
    return list(set(images))  # 去重


def get_image(referer, url):
    u = urlsplit(url)  # schema, netloc, path, query, fragment
    filename = split(u[2])[1]
    header = default
    header["Referer"] = referer
    header["Host"] = u[1]
    # header["X-Requested-With"] = "XMLHttpRequest"
    response = do_request(url, header)
    return {"filename": filename, "data": response.read()}
