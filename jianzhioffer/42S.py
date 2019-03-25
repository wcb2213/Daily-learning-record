#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/25


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        res = []
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                if array[i] + array[j] == tsum:
                    res.append(array[i])
                    res.append(array[j])
                    # res.append([array[i], array[j]]) # 不一样
                    return res
        return []