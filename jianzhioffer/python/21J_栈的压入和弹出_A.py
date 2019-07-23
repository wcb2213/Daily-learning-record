#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/17


# 33ms
# 栈的压入和弹出
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        while pushV:
            stack.append(pushV.pop)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop
        if stack:
            return False
        return True