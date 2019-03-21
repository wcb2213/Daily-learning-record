#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/17


import sys

n = int(sys.stdin.readline())
L1, L2 = [], []
for i in range(n):
    L = []
    L = list(map(int, sys.stdin.readline().split()))
    L1.append(L[0])
    L2.append(L[1])

# 去除 pos_num-neg_num-1 个最远的苹果树的苹果数量
def tree_not_touch(A):
    res = sum(L2)
    B = []
    for i in range(0, abs(pos_num-neg_num-1)):
        B.append(A[i])
    for i in B:
        for j in range(n):
            if L1[j] == i:
                 res -= L2[j]
    return res

# 计算坐标方向。如正数为正方向数量
pos_num = 0
for i in L1:
    if i > 0:
        pos_num += 1
neg_num = n-pos_num

# 如果正数个数与负数个数相差1及以内 输出 sum（L2）
if (pos_num-neg_num>=-1) and (pos_num-neg_num<=1):
    print(res)

# 正数多，正数多算一个
elif pos_num > neg_num:
    A = sorted(L1, reverse=True)
    print(tree_not_touch(A))

# 负数多，负数多算一个
elif pos_num < neg_num:
    A = sorted(L1, reverse=False)
    print(tree_not_touch(A))