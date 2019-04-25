#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/25


# 35ms
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        res = []
        for i in array:
            if i > tsum//2+1:
                break
            if tsum - i in array:
                res.append(i)
                res.append(tsum-i)
        return res[:2]