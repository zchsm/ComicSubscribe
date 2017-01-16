#!/usr/share/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser
from os.path import exists, dirname, expanduser
from os import makedirs, mkdir


class Config(ConfigParser):
    def __init__(self, path):
        super(Config, self).__init__()
        self.path = expanduser(path)
        self.load()

    def load(self):
        if not exists(dirname(self.path)):
            mkdir(dirname(self.path))

        if not exists(self.path):
            self.add_section("Config")
            self.set("Config", "download", expanduser("~/Comic/download"))
            self.set("Config", "list", expanduser("~/Comic/list.csv"))

            makedirs(dirname(self.path), exist_ok=True)
            with open(self.path, "w") as f:
                self.write(f)
        else:
            self.read(self.path, "utf-8")

        list_file = self.get("Config", "list")
        if not exists(list_file):
            open(list_file, "a").close()

        download_folder = self.get("Config", "download")
        if not exists(download_folder):
            mkdir(download_folder)

config = Config("~/Comic/config")
setting = {key: value for key, value in config.items("Config")}
