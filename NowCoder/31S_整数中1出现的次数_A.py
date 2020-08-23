#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


# 30ms
# 整数中1出现的个数
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        return ''.join(map(str, range(n+1))).count('1')

    # 或者从数字规律着手