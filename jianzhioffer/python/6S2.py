#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/17


# 687ms
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i] > rotateArray[i+1]:
                return rotateArray[i+1]