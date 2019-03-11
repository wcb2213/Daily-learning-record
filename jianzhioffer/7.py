#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


class Solution:
    def Fibonacci(self, n=39):
        # write code here
        f0, f1 = 0, 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for i in xrange(2, n+1):
            a = f0 + f1
            f0 = f1
            f1 = a
        return a