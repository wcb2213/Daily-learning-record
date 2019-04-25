#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/25


# 29ms
# 排序数组？
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        a = -1
        for i in range(len(data)):
            if data[i] == k:
                a = i
                break
        if a == -1:
            return 0
        for i in range(i,len(data)):
            if data[i] != k:
                b = i
                break
        try:
            return b-a
        except:
            return len(data)-a