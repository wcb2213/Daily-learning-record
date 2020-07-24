#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/25


# 34ms
# 和为S的两个数字
# 哈希或者双指针，没有二分
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array: return []
        i,j=0,len(array)-1
        while i<j:
            if array[i]+array[j]<tsum:
                i+=1
            elif array[i]+array[j]>tsum:
                j-=1
            else:
                return [array[i],array[j]]
        return []