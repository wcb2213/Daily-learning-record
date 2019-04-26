#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/31


# 23ms
# 字符串中第一个重复的字符
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.s.count(i) == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char