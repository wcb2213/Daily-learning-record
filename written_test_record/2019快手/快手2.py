#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/13


# 90%
# l = 0,1,2,3,4,5,7
# input
l = list(map(int, input().split(',')))

# process
a = 1
i = 0
while a:
    if i not in l:
        print(i)
        a = 0
    i += 1
    if i > len(l)+1:
        a = 0