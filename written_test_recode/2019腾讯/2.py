#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


# input
n = int(input())
s = input().split(' ')
inputL = []
for i in range(n):
    inputL.append(int(s[i]))

# process
money = 0
def test(i):
    global money
    if inputL[i] > 0:
        money += inputL[i]
        inputL[i+1] += inputL[i]
    else:
        money -= inputL[i]
        inputL[i + 1] += inputL[i]

# main
for i in range(n-1):
    test(i)
money += abs(inputL[n-1])
print(money)