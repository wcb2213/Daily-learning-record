#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16


class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, node):
        # write code here
        min = self.min()
        if not min or min>node:
            self.minstack.append(node)
        else:
            self.minstack.append(min)
        self.stack.append(node)

    def pop(self):
        # write code here
        if self.stack:
            self.minstack.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.minstack:
            return self.minstack[-1]