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
        if n <= 1: return n
        a, b = 0, 1
        for i in range(2,n+1):
            a, b = b, a + b
        return b