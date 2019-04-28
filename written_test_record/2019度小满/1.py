#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/28


n = int(input())
l1,l2 = [],[]
for i in range(n):
    a,b = map(int,input().split(' '))
    l1.append(a)
    l2.append(b)

nmax = max(l1)
l2 = sorted(l2)
for i in range(len(l2)):
    if l2[i] > nmax:
        break
print(n-i)