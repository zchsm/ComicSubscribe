#!/user/share/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse
from gzip import decompress

default = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,en-US;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
}


def do_request(url, header=None):
    if header is None:
        header = default
    try:
        url = parse.quote(url, safe="/:?=&")
        req = request.Request(url, headers=header)
        res = request.urlopen(req, timeout=20)
        return res
    except Exception as e:
        print(e)


def get_content(url, header=None):
    response = do_request(url, header)
    content = decompress(response.read())
    return content.decode("utf-8", "ignore")


def save_image(file, content):
    with open(file, "wb") as f:
        f.write(content)
