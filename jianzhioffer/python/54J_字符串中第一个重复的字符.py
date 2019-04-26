#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/31

# 30ms
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'
    # 创建字典给每个字符计数 char为单个字符
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1