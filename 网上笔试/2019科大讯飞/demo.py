#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/11


while 1:
    a = []
    s = input()

    if s != "":
        for x in s.split():
            a.append(int(x))

        print(sum(a))
    else:
        break