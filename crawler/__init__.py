#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from crawler.comic import Comic
from crawler.utils import save_image
from config import setting
from urllib import parse
from os import mkdir, walk, chdir, listdir
from os.path import exists, join, isdir, split
import zipfile


def download(comic_url, path):
    c = Comic()
    chapter_dict = c.get_comic(comic_url)
    print("下载漫画到目录 {}/".format(path))
    for chapter_url, chapter_name in chapter_dict.items():
        chapter_path = join(path, chapter_name)
        if not exists(chapter_path):
            mkdir(chapter_path)
        image_list = c.get_chapter(comic_url, chapter_url)
        print("下载章节 {}".format(chapter_name))
        for image_url in image_list:
            image_data = c.get_image(chapter_url, image_url)
            save_image(join(chapter_path, image_data["filename"]), image_data["data"])


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


def create_zip(folder):
    zipf = zipfile.ZipFile(folder + ".zip", 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in walk(folder):
        for file in files:
            zipf.write(join(root, file))


def compress(path):
    print("开始为每一章节生成压缩文件")
    chdir(path)
    for d in listdir(path):
        if isdir(d):
            folder = split(d)[1]
            print("压缩章节 {}".format(folder))
            create_zip(folder)


def crawler():
    it = read()
    for u in it:
        print(u)
        p = analyse(u)
        download(u, p)
