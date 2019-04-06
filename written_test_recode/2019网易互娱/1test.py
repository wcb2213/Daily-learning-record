#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/6


from functools import reduce
t = 4
n = 7
l1 = [1,2,3,4,5,6,7]
l1Min = min(l1)
l1Max = max(l1)
def mutip(a, b):
    return a*b
num = 0
if l1Max - l1Min >= 4:
    l1Height = [0 for i in range(l1Max - l1Min + 1)]
    for i in range(len(l1Height)):
        l1Height[i] = l1.count(l1Min+i)
    print(l1Height)
    for i in range(0, l1Max - l1Min - 3):
        for j in range(l1Max - l1Min - 3 - i):
            num += reduce(mutip, l1Height[0+j:5+j+i])

print(num)