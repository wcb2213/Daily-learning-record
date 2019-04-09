#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/24


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        #tmp = set()
        tmp = []
        for a in array:
            if a in tmp:
                tmp.remove(a)
            else:
                tmp.append(a)
        return tmp
        #return list(tmp)