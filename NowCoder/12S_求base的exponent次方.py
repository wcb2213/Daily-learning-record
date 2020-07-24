#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


# 28ms
# 求base的exponent次方  代码的完整性
class Solution:
    def Power(self, base, exponent):
        result = 1
        if base==0 and exponent==0:
            raise Exception("无意义")
        if exponent == 0:
            return 1
        if base==0 and exponent<0:
            raise Exception("输入错误")
        if exponent < 0:
            for i in range(-exponent):
                result *= base
            return 1/result
        for i in range(exponent):
            result *= base
        return result
a = Solution()
print(a.Power(0,0))