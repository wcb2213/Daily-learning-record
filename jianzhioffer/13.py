#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


class Solution:
    def reOrderArray(self, array):
        # write code here
        s1, s2 = [], []
        for i in array:
            if i%2==0:
                s2.append(i)
            else:
                s1.append(i)
        s1.extend(s2)
        return s1

# 第一种
# s1, s2 = [], []
# s2.append(1)
# s1.extend(s2)
# print(s1)
# 第二种
# s3 = s1 + s2
# print(s3)