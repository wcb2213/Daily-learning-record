#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


n = 4
l1 = [1, 2, 4, 9]
l2 = [1, 1, 1, 1]
res = []
for i in range(n):
    res.append(abs(l1[i]-i-1) + abs(l2[i]-1))