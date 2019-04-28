#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/28


n=3
l=[1, 2, 1]

res = []
for i in range(1, n):
    a = 0
    l1 = l[i:]
    for j in range(i):
        a += n-i-l1.count(l[j])
    res.append(a)

for i in range(len(res)-1):
	print(res[i],end=' ')
print(res[-1],end='')