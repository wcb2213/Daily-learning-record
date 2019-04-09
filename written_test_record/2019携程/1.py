#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/8

# input
s = input().split(',')
l = []
for i in s:
    l.append(i)

# main
b = 0
for i in range(len(l)):
    a = l.count(l[i])
    if a > 1:
        b = 1
if b == 1:
    print('true')
else:
    print('false')