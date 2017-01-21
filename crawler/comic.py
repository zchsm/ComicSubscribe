#!/user/share/env python3
# -*- coding: utf-8 -*-

from crawler.modules import get_module
from os.path import exists
from os import mkdir


class Comic(object):

    def __init__(self):
        self.url = ""
        self.module = None

    def init_module(self, url):
        if not self.module:
            module = get_module(url)
            if not module:
                print("不支持的网站")
                exit(1)
            self.url = url
            self.module = module

    # 获取漫画所有章节URL列表
    # dict类型，{url1: title1, url2: title2, ...}
    def get_comic(self, url):
        self.init_module(url)
        return self.module.get_comic(url)

    # 获取某一章节所有图片URL列表
    # list类型，[url1, url2, url3, ...]
    def get_chapter(self, referer, url):
        self.init_module(referer)
        return self.module.get_chapter(referer, url)

    # 获取某一张图片
    # dict类型，{"filename": filename, "data": data}
    def get_image(self, referer, url):
        self.init_module(referer)
        return self.module.get_image(referer, url)
