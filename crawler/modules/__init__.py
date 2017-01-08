#!/usr/share/env python3
# -*- coding: utf-8 -*-

from os.path import dirname, splitext
from os import listdir
from importlib import import_module
import re

path = dirname(__file__)

module_info = {}

modules = set()
for file in listdir(path):
    name, extension = splitext(file)
    if name == "__init__" or extension != ".py":
        continue
    modules.add(import_module("crawler.modules." + name))


def get_module(url):
    match = re.search(r"https?://([^/]+?)/", url)
    if not match:
        return None
    for module in modules:
        if match.group(1) == module.domain:
            return module
    return None
