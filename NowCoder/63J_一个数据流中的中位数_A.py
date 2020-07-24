#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


# 36ms
# 一个数据流中的中位数
class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self, data):
        # write code here
        n = len(self.data)
        if n % 2 == 1:
            return self.data[(n-1)/2]
        else:
            return (self.data[n/2] + self.data[n/2-1])/2.0