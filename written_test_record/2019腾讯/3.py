#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


# 20% 超时!
# input
s1 = input().split(' ')
n = int(s1[0])
k = int(s1[1])
s2 = input().split(' ')
inputL = []
for i in range(n):
    inputL.append(int(s2[i]))
# process
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
    for j in range(len(inputL)):
        inputL[j] -= minN
    return
# main
for i in range(k):
    test()
