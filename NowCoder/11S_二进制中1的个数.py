#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/25


# 25ms
# 二进制中1的个数 转换成字符串在计算
class Solution:
    def NumberOf1(self, n):
        # write code here
        # s = bin(n) if n>=0 else bin(n+(2**32))
        # s = bin(n) if n>=0 else bin(n & 0xffffffff)
        s = bin(n&(2**32-1))
        return s.count('1')

## 二进制
# 正数 原码， 负数 补码
# python bin函数得到的字符串 正数 0b原码， 负数 -0b正数（负数相反数）的原码##java中直接显示为补码
# print(bin(-3)) #-0b11
# print(bin(-3 & 0xffffffff)) #0b11111111111111111111111111111101
# python 负数的二进制改成补码有两种方法：
## 1 负数补码=2**32+n  不懂
## 2 bin(n & 0xffffffff)
