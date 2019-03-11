#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/11


import math

while 1:
    s = input()
    L = []

    if s !='':
        for i in s.split():
            L.append(int(i))
        n = L[0]
        m = L[1]
        L2 = []
        for i in range(m):
            L2.append(n)
            n = math.sqrt(n)
        print('%.2f' % sum(L2))
    else:
        break