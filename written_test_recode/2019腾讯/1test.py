#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


n = 15
k = 4

a = n
b = 0
for i in range(k):
    a = (a+1)//2
    if a == 1:
        b = i+1
if b != 0:
    print(b+1)
else:
    print(a+k)