#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


# 29ms
# 矩阵覆盖 同 7 斐波那契数列
class Solution:
    def rectCover(self, number):
        # write code here
        n = number
        L = [0, 1, 2]
        for i in range(3, n + 1):
            L.append(L[i - 2] + L[i - 1])
        return L[n]