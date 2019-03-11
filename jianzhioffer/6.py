#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/23


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        return min(rotateArray)