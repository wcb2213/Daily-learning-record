#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/3


# 2. O(logn) 二分法
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0: return 0
        i,j=0,len(rotateArray)-1
        while i<j: #旋转数组可以不旋转，且二分后仍为旋转数组
            if rotateArray[i]<rotateArray[j]: break
            mid = (i+j)//2
            if rotateArray[mid]>rotateArray[j]:
                i=mid+1
            elif rotateArray[mid]<rotateArray[j]:
                j=mid
            elif rotateArray[mid]==rotateArray[j]:
                i+=1
        return rotateArray[i]