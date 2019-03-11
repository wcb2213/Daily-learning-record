#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


class Solution:
    def NumberOf1(self, n):
        # write code here
        return bin(n).replace("0b","").count("1") if n>=0 else bin(2**32+n).replace("0b","").count("1")


# 正数的补码 = 原码
# 负数的补码 = {原码符号位不变} + {数值位按位取反后+1}
#
# 1、一个负整数（或原码）与其补数（或补码）相加，和为模。
# 2、对一个整数的补码再求补码，等于该整数自身。
# 3、补码的正零与负零表示方法相同。
#
# 负数的原码的绝对值 + 补码 = 模 即2^n
# 例如 2^4—|—5|=11=1011

