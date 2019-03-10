#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        else:
            return pow(2,number-1)


# 所以f(n)=f(n-1)+f(n-2)+...+f(1)+1
# 因为f(n-1)=f(n-2)+f(n-3)+...+f(1)+1
# 所以f(n)=2*f(n-1)