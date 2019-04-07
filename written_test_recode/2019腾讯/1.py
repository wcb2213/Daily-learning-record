#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


# 这个应该100%了
s = input().split(' ')
n = int(s[0])
k = int(s[1])
# print(n)

a = n
b = 0
for i in range(k):
    a = (a+1)//2
    if a == 1:
        b = i+1
        # b = i 忘记加1  最后80%
if b != 0:
    print(b+1)
else:
    print(a+k)