#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/20


# 剪绳子
# 给定一个正整数 n，将其拆分为至少两个正整数的和，
# 并使这些整数的乘积最大化。
# 前提：不论是几个数相乘积最大，这些数的最大值不会大于 n//2+1
def func(n):
    l = [0,0,1]
    for i in range(3, n+1):
        m = 0
        for j in range(1,i):
            m = max(m,j*(i-j),j*l[i-j])
        l.append(m)
    return l[n]

print(func(8))