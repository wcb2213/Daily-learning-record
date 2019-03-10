#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


class Solution:
    def Power(self, base, exponent):
        result = 1
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        if exponent < 0:
            for i in range(-exponent):
                result = result * base
            return 1/result
        for i in range(exponent):
            result = result * base
        return result