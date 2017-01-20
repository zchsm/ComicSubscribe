#!/usr/share/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from os.path import exists, dirname, expanduser, split, join
from os import makedirs, mkdir


class Config(ConfigParser):
    def __init__(self, path):
        super(Config, self).__init__()
        self.path = expanduser(path)
        self.load()

    def load(self):
        comic_home, config_file = split(self.path)
        if not exists(comic_home):
            makedirs(comic_home)

        if not exists(self.path):
            self.add_section("Config")
            self.set("Config", "download", expanduser(join(comic_home, "download")))
            self.set("Config", "list", expanduser(join(comic_home, "list.txt")))

            with open(self.path, "w") as f:
                self.write(f)
            print("生成配置文件 {}".format(self.path))
        else:
            self.read(self.path, "utf-8")

        list_file = self.get("Config", "list")
        if not exists(list_file):
            open(list_file, "a").close()
            print("创建漫画列表文件 {}, 在文件中记录需要下载的漫画列表".format(list_file))

        download_folder = self.get("Config", "download")
        if not exists(download_folder):
            mkdir(download_folder)

config = Config("~/Comics/config")
setting = {key: value for key, value in config.items("Config")}
