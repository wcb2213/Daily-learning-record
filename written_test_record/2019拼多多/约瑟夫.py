#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/10

def f(n):
    if n==1:
        return [1]
    if n==2:
        return [1,2]
    L=[]
    R=[]
    for i in range(1, n+1):
        L.append(i)
    while len(L)>=3:
        R.append(L.pop(0))
        L.append(L.pop)
    if len(L)==1:
        R.append(L[0])
    if len(L)==2:
        R.append(L[0])
        R.append(L[1])
    return R
L = f(int(input()))
for i in range(len(L)):
    print(L[i], end=' ')