#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/5


m, n = 20, 4
l = [1, 2, 5, 10]
# s = input().split(' ')
# m = int(s[0])
# n = int(s[1])
# l = []
# for i in range(n):
#     l.append(int(input()))

def lessNumCoin(a, n, m, coinIndex):
    if a == 0:
        return
    for i in range(n):
        if a >= l[n-1 - i]:
            coinIndex = n-1 - i
            global lcoinNum
            lcoinNum[n-1 - i][m-1] += 1
            a -= l[coinIndex]
            global num
            num += 1
            return lessNumCoin(a, n, m, coinIndex)
    num -= 1
    return lessNumCoin(a+l[coinIndex], coinIndex, m, coinIndex)

lcoinNum = [ [0 for i in range(m)] for i in range(n)]
res = []
for i in range(1, m+1):
    num = 0
    lessNumCoin(i, n, i, 0)
    res.append(num)
print(res)
print(lcoinNum)
print(max(lcoinNum[0]) + max(lcoinNum[1]) + max(lcoinNum[2]) + max(lcoinNum[3]))


