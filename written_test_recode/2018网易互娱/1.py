#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


# 复杂度超了
# n = 4
# l = [1, 2, 3, 4]
n = int(input())
l = list(map(int, input().split(' ')))

b = []
for i in range(n):
    b.append(l[i])
    b.reverse()
for i in range(n-1):
    print(b[i], end=' ')
print(b[n-1], end='')