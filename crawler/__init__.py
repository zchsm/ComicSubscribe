#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crawler.comic import Comic
from crawler.crawler import save_image
from config import setting
from os.path import exists
from urllib import parse
from os.path import join
from os import mkdir


def download(comic_url, path):
    c = Comic()
    chapter_dict = c.get_comic(comic_url)
    for chapter_url in chapter_dict:
        image_list = c.get_chapter(comic_url, chapter_url)
        for image_url in image_list:
            image_data = c.get_image(chapter_url, image_url)
            save_image(join(path, image_data["filename"]), image_data["data"])


def read():
    path = setting["list"]
    with open(path, "r") as f:
        for url in f:
            yield url.rstrip("\n")


def analyse(comic_url):
    folder = parse.urlsplit(comic_url)[2]
    path = join(setting["download"], str(folder).strip("/\n"))
    if not exists(path):
        mkdir(path)
    return path
