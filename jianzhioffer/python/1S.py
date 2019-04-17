#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/13


# 二维数组的查找
# 220ms
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n = len(array)
        for i in range(n):
            if target in array[i]:
                return True
        return False