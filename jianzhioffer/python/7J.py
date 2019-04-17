#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


# 26ms 时间更短
# 斐波那契数列的第n项
# 虽然是递归思想，但不推荐递归函数
class Solution:
    def Fibonacci(self, n):
        # write code here
        L = [0, 1, 1]
        a = 3
        while n > a-1:
            L.append(L[a-2]+L[a-1])
            a += 1
        return L[n]