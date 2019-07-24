#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


# 23ms
class Solution:
    def jumpFloorII(self, number):
        # write code here
        n = number
        l = [0,1,2]
        index = 2
        while n>index:
            l.append(sum(l)+1)
            index += 1
        return l[n]