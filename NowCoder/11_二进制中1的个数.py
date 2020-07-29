#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/25


# emm 超时。。
# 二进制中1的个数 使用位运算
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            n = n&(n-1) #把一个整数减去1之后与原来的整数做二进制与运算，相当于把这个整数最右边的1变为0
            count += 1
        return count

# 正数的原码，补码，反码 相同
# 负数的原码，符号位改为1
#       反码，符号位不变，其余取反
#       补码，反码+1
#   eg：5   表示为 0000 0101
#       -5  表示为（ 原码）：1000 0101 ===>  反码 ：1111 1010  ===>  补码：1111 1011
# 二进制中1的个数 转换成字符串在计算

class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n&0xffffffff).count("1")

## 二进制
# 正数 原码， 负数 补码  实际上python的数字均已补码形式存在

# python bin函数得到的字符串 正数 0b原码， 负数 -0b正数（负数相反数）的原码##java中直接显示为补码
# print(bin(-3)) #-0b11

# python 负数的二进制改成补码：
# bin(n & 0xffffffff)
# print(bin(-3 & 0xffffffff)) #0b11111111111111111111111111111101