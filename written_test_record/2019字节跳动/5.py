#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/14


t = int(input())
n ,p = [], []
for i in range(t):
    n.append(int(input()))
    p.append(list(map(int, input().split(' '))))
# print(n, p)
# t = 2
# n, p = [2, 4], [[1, 2], [4, 3, 2, 1]]

def f1(n, p):
    if n == 2 or n == 3:
        return p[0]
    else:
        return p[0]+sum(p[1:-2])+(n-3)*p[-2]

for i in range(t):
    print(f1(n[i], sorted(p[i], reverse=True)))