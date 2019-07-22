#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/13


# 311ms
# 二维数组的查找
# 书T4
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        n = 0
        m = len(array[0]) - 1
        while n<len(array) and 0<=m:
            if array[n][m] == target:
                return True
            if array[n][m] > target:
                m -= 1
            elif array[n][m] < target:
                n += 1
        return False
