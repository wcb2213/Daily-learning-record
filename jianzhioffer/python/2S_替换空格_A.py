#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/14


# 23ms
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = list(s) # 方便置换 s[i] str有切片 但是不能赋值
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)
