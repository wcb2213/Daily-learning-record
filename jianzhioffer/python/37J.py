#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/25


# 27ms
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        flag = 0
        for i in range(len(data)):
            if data[i] == k:
                flag += 1
        return flag