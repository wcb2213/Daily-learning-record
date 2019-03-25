#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/25


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # if tsum <= 2:
        #     return []
        res = []
        for i in range(1, tsum//2+1):
            for j in range(i+1, tsum//2+2):
                tmp = (i+j)*(j-i+1)/2
                if tmp == tsum:
                    res.append(list(range(i,j+1)))
        return res
