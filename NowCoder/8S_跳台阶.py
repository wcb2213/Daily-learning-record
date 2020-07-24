#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/24


# 25ms
# 跳台阶
class Solution:
    def jumpFloor(self, number):
        # write code here
        n = number
        l=[0,1,2,3]
        index = 3
        while n>index:
            l.append(l[index]+l[index-1])
            index += 1
        return l[n]