#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


# 26ms
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的
# min函数（时间复杂度应为O（1））。
class Solution:
    def __init__(self):
        self.stack = [] # 同长度的两个list
        self.minstack = []

    # 定义栈的数据结构
    def push(self, node):
        # write code here
        self.stack.append(node)
        min = self.min()
        if not min or min >= node:
            self.minstack.append(node)
        else:
            self.minstack.append(min)
    def pop(self):
        # write code here
        if self.stack:
            self.minstack.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    # min函数
    def min(self):
        # write code here
        if self.minstack:
            return self.minstack[-1]