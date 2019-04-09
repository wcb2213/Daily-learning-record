#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/23


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray==[]:
            return 0
        i = 0
        while 1:
            if rotateArray[i]-rotateArray[i+1] > 0:
                return rotateArray[i+1]
            i = i+1

# 运行时间：929ms
#
# 占用内存：5736k