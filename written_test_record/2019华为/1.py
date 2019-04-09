#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/27


n = int(input())
# s = "0abcdefgh1abcdefgh"
s = input()
a = []
b = []
for i in range(n):
    a.append(s[i*9:(i*9+9)])
for m in a:
    if m[0] == "1":
        b.append(m[1:9])
    if m[0] == "0":
        c = m[1:9]
        b.append(c[::-1])
print(' '.join(b))
#print(b[0] + " " + b[1])