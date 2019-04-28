#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/28


n=4
l1=[4, 2, 2, 1]
l2=[7, 6, 5, 2]


nmax = max(l1)
l2 = sorted(l2)
for i in range(len(l2)):
    if l2[i] > nmax:
        break
print(n-i)