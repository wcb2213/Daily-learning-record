#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


class Solution:
    def jumpFloorII(self, number):
        # write code here
        n = number
        if n == 1:
            return 1
        elif n == 2:
            return 2
        s = [0]*(n+1)
        s[1] = 1
        s[2] = 2
        for i in range(3, n+1):
            s[i] = 1
            for j in range(1, i):
                s[i] = s[i] + s[j]
        return s[n]

A = Solution()
c = A.jumpFloorII(3)
print(c)