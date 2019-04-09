#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size <= 0 or size > num:
            return []
        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i:i+size]))
        return res