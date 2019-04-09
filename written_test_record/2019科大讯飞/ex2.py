#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/11


import math

while 1:
    s = input()
    L = []

    if s !='':
        for i in s.split():
            L.append(int(i))
        m = L[0]
        n = L[1]
    else:
        break

    if 100<=m<=n<=999:
        L2 = []
        for i in range(m, n+1):
            a=int(i/100)
            b=int(i/10)-10*a
            c=i%10
            if i == pow(a,3)+pow(b,3)+pow(c,3):
                L2.append(i)
        if L2:
            for i in L2:
                print(i, end=' ')
        else:
            print('no')
    else:
        break