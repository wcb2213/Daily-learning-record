#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


# 25ms
class Solution:
    def __init__(self):
        self.arr=[]
    def push(self, node):
        # write code here
        self.arr.append(node)
    def pop(self):
        # write code here
        return self.arr.pop()
    def top(self):
        return self.arr[-1]
    def min(self):
        # write code here
        return min(self.arr)