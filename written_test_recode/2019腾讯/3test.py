#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


n, k = 4, 1
inputL = [5, 5, 7, 2]

def test():
    if inputL.count(0) == n:
        print(0)
        return
    minN = 0
    inputL.sort()
    i = 0
    while minN <=0 and i <= n-1:
        minN = inputL[i]
        i += 1
    if minN <= 0:
        return
    print(minN)
    for i in range(len(inputL)):
        inputL[i] -= minN
    return
for i in range(k):
    test()