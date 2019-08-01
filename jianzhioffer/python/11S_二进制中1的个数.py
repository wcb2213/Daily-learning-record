#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/25


# 25ms
# 二进制中1的个数
class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n&(2**32-1)).replace('0b','').count('1')