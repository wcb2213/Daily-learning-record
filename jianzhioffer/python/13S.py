#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24



# 26ms
class Solution:
    def reOrderArray(self, array):
        # write code here
        s1, s2 = [], []
        for i in array:
            if i%2==0:
                s2.append(i)
            else:
                s1.append(i)
        return s1+s2
