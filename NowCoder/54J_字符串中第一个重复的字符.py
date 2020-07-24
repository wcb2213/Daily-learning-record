#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/31

# 30ms
class Solution:
    # 返回对应char
    def __init__(self):
        self.ss=''
        self.dic={}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.ss:
            if self.dic[i]==1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.ss += char
        if char in self.dic:
            self.dic[char]+=1
        else:
            self.dic[char]=1