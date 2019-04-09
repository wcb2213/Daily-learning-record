#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/6


# 30% 估计超时了
from functools import reduce

# input
t = int(input())
inputL = []
for i in range(t):
    inputL.append(int(input()))
# print(inputL)

# process
def trans(a):
    # 1
    aStr = str(a)
    aLen = len(str(a))
    n = (aLen + 2) // 3
    if aLen / 3 == n:
        l1 = [aStr[i * 3:(i + 1) * 3] for i in range(n)]
    else:
        nnn = 3 * n - aLen
        l1 = [aStr[3 - nnn + i * 3:3 - nnn + (i + 1) * 3] for i in range(n - 1)]
        l1.insert(0, aStr[0: 3 - nnn])
    # print(l1)

    # 2
    def f1(s):
        return str(bin(int(s))[2:])
    l1 = list(map(f1, l1))
    # print(l1)['10', '101100011']

    # 3
    def f2(s):
        n = len(s)
        return (5 - n) * '0' + s

    l2 = []
    for i in range(len(l1)):
        if len(l1[i]) == 10:
            l2.append(l1[i][0:5])
            l2.append(l1[i][5:10])
        elif len(l1[i]) <= 5:
            l2.append(f2(l1[i]))
        else:
            n = len(l1[i])
            l2.append(f2(l1[i][0:n - 5]))
            l2.append(f2(l1[i][n - 5:n]))
    # print(l2)

    # 4
    def f3(s):
        return int(s, 2)

    l3 = list(map(f3, l2))
    # print(l3)

    # 5
    dict = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', '16': 'G', '17': 'H',
            '18': 'I', '19': 'J', '20': 'K', '21': 'L', '22': 'M', '23': 'N', '24': 'O', '25': 'P',
            '26': 'Q', '27': 'R', '28': 'S', '29': 'T', '30': 'U', '31': 'V'}

    def f4(s):
        if s in dict:
            return dict[s]
        return s

    def f5(s1, s2):
        return s1 + s2

    l4 = list(map(f4, map(str, l3)))
    # print(l4)['5', 'H', 'B']
    l5 = reduce(f5, l4)
    print(l5)

# main
for i in range(t):
    trans(inputL[i])