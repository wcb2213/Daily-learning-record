#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/22


# 22ms
# 用两个栈来实现一个队列 容量为 2n+1 (n为较小的栈的容量)
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if not self.Stack2:
            while self.Stack1:
                self.Stack2.append(self.Stack1.pop())
        return self.Stack2.pop()
