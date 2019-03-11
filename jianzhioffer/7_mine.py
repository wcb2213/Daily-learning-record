#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


class Solution:
    def Fibonacci(self, n):
        # write code here
        L = [0, 1, 1]
        a = len(L)
        while n>a-1:
            L.append(L[a-2]+L[a-1])
            a=a+1
        return L[n]


# 运行时间：23ms
#
# 占用内存：5728k