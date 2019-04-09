#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/10

import sys_test
# for line in sys.stdin:
#     a = line.split()
# n = int(sys.stdin.readline())
#
# for i in range(n):
#     # 读取每一行
#     line = sys.stdin.readline().strip()
#     # 把每一行的数字分隔后转化成int列表
#     values = list(map(int, line.split()))

import sys_test
for line in sys_test.stdin:
    n, d = line.split()
    print(n, d)
