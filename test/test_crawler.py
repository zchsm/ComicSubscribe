#!/usr/share/env python
# -*- coding: utf-8 -*-

from crawler import download, analyse, read

it = read()
for u in it:
    print(u)
    p = analyse(u)
    download(u, p)




