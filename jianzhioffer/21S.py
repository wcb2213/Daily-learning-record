#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/17


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        while pushV:
            stack.append(pushV.pop(0))
        # for i in pushV:
        #     stack.append(i)

            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if stack:
        # if len(stack):
            return False
        return True
