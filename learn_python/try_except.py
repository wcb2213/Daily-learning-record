#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/10/30


##  剑指offer 第一题
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag = 'false'
        n=len(array)
        for i in range(n):
            if target in array[i]:
                flag='true';
                break
        return flag
while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(str(input())))
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break