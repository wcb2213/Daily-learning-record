#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/6/13


## 1.两个栈实现一个队
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
## 2.两个队实现一个栈
class Solution:
    def __init__(self):
        self.Queue1=[]
        self.Queue2=[]
        self.flag = True ## queue1空为True,queue可能同时为空
    def push(self,node):
        if self.flag:
            self.Queue1.append(node)
        else:
            self.Queue2.append(node)
    def pop(self):
        if self.flag:
            while len(self.Queue2)!=1:
                self.Queue1.append(self.Queue2.pop(0))
            self.flag = False
            return self.Queue2.pop(0)
        else:
            while len(self.Queue1)!=1:
                self.Queue2.append(self.Queue1.pop(0))
            self.flag = True
            return self.Queue1.pop(0)
