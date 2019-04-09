#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/7


n = 5
inputL = [5, -4, 1, -3, 1]

money = 0
def test(i):
    global money
    if inputL[i] > 0:
        money += inputL[i]
        inputL[i+1] += inputL[i]
    else:
        money -= inputL[i]
        inputL[i + 1] += inputL[i]

for i in range(n-1):
    test(i)
print(money)