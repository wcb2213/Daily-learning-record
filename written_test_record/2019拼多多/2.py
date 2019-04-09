#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/10


import sys_test


a=sys_test.stdin.readline()
a=a.lower()
l=[]
for i in a:
    l.append(i)
s=set(l)
l2=list(s)
# print(l2, type(l2[0]))
# ['a', 'y', 'x', 'b'] <class 'str'>

result=min(l2)
print(result, type(result))

