#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/13


# 311ms
# 二维数组的查找
# 注意    尽量选择单条流程（右上开始）
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        i = 0
        j = len(array[0]) - 1
        while i<=len(array)-1 and 0<=j:
            if array[i][j] == target:
                return True
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
        return False
