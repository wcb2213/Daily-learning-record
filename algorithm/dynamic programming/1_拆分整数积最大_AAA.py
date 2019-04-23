#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/20


# 给定一个正整数 n，将其拆分为至少两个正整数的和，
# 并使这些整数的乘积最大化。
#
# 前提：不论是几个数相乘积最大，这些数的最大值不会大于 n//2+1
def func(n):
    l = [1] # n=2
    for i in range(3,n+1):
        m = 0
        for j in range(1,i//2+1):
            m = max(m,j*(i-j),j*l[i-j-2]) # func（10）存储在l[8]
        l.append(m)
    return l
print(func(10))