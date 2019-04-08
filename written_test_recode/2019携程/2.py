#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/8


# 8.33%?
# input
s = input().split(',')
l = []
l.append(int(s[0][1]))
for i in s[1:-1]:
    l.append(int(i))
l.append(int(s[-1][0]))
k = int(input())

# main
res = []
n = len(l)
if k>n or k==1:
    print(str(l).replace(' ', ''))
else:
    a = n//k
    for i in range(a):
        lRev = l[i*k:(i+1)*k]
        lRev.reverse()
        res += lRev
    res += l[a*k:]
    print(str(res).replace(' ', ''))