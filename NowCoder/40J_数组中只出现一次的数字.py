#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/24


# 32ms
# 数组中只出现一次的数字
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic={}
        for i in array:
            dic[i] = not (i in dic)
        res=[]
        for k,v in dic.items():
            if v:
                res.append(k)
        return res
