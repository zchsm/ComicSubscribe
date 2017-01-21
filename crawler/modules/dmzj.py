#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import execjs
from crawler.utils import get_content, do_request, default, get_image_name
from urllib.parse import urljoin, urlsplit
import json

domain = "manhua.dmzj.com"


def get_comic(url):
    content = get_content(url)
    scope_pattern = re.compile(r"<div class=\"cartoon_online_border\" (style=\"display:none\")?>.*?<ul>(.*?)</ul>", re.S)
    # chapters_content = scope_pattern.search(content)
    chapters_content_it = scope_pattern.finditer(content)
    chapters = []
    for chapters_content in chapters_content_it:
        chapters_pattern = re.compile(r"<a title=\"(.*?)\" href=\"(.*?)\"", re.S)
        chapters += chapters_pattern.findall(chapters_content.group(2))
    return {urljoin(url, c[1]): c[0] for c in chapters}


# http://images.dmzj.com/y/%E4%B8%80%E6%8B%B3%E8%B6%85%E4%BA%BA/5/02.jpg
def get_chapter(referer, url):
    header = default
    header["Referer"] = referer
    header["Host"] = domain
    content = get_content(url, header)
    function_pattern = re.compile(r"eval\((function\(.*?)\)\s+;", re.S)
    function_content = function_pattern.search(content)
    if not function_content:
        return []
    result = execjs.eval(function_content.group(1))

    url_pattern = re.compile(r"(\[.*?\])", re.S)
    url_content = url_pattern.search(result)
    if not url_content:
        return []
    images = json.loads(url_content.group(1))
    return [urljoin("http://images.dmzj.com", i) for i in images]


def get_image(referer, url):
    filename = get_image_name(url)
    header = default
    header["Referer"] = referer
    header["Host"] = "images.dmzj.com"
    response = do_request(url, header)
    return {"filename": filename, "data": response.read()}

