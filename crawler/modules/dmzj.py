#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import execjs
from crawler.utils import get_content, do_request, default
from urllib.parse import urljoin, urlsplit
from os.path import split

domain = "manhua.dmzj.com"


def get_comic(url):
    content = get_content(url)
    scope_pattern = re.compile(r"<div class=\"cartoon_online_border\" >.*?<ul>(.*?)</ul>", re.S)
    chapters_content = scope_pattern.search(content)
    if not chapters_content:
        return {}
    chapters_pattern = re.compile(r"<a title=\"(.*?)\" href=\"(.*?)\"", re.S)
    chapters = chapters_pattern.findall(chapters_content.group(1))
    return {urljoin(url, c[1]): c[0] for c in chapters}


def get_chapter(referer, url):
    pass
