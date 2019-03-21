#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/10

import sys_test


n = int(sys_test.stdin.readline())
l1 = list(map(int, sys_test.stdin.readline().split()))
l2 = list(map(int, sys_test.stdin.readline().split()))

l1.sort(reverse=True)
l2.sort(reverse=False)

s=0
for i in range(n):
    s=s+l1[i]*l2[i]
print(s)
