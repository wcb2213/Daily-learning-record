#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/18

# 30ms
# 调整数组序列 列表生成式
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array) == 0:
            return []
        l1 = [i for i in array if i%2 == 1]
        l2 = [i for i in array if i%2 == 0]
        return l1+l2