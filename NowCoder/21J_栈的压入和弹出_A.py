#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/17


# 33ms
# 栈的压入(for一个一个压)和弹出(while一直弹)
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack,i=[],0
        for j in range(len(pushV)):
            stack.append(pushV[j])
            while stack and stack[-1]==popV[i]:
                i+=1
                stack.pop()
        return not stack