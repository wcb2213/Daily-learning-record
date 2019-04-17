#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/15


# 25ms
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        L = []
        head = listNode
        while head:
            L.insert(0, head.val)
            head = head.next
        return L

# aList = [123, 'xyz', 'zara', 'abc']
# aList.insert( 3, 2009)
# print "Final List : ", aList
# Final List : [123, 'xyz', 'zara', 2009, 'abc']  # 将L[3]挤到右边