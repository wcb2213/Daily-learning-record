#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/15


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        L = []
        head = listNode  #### 创建指针类  最后一个为  val 但 next 指向 None
        while head:
            L.insert(0, head.val)
            head = head.next
        return L


# aList = [123, 'xyz', 'zara', 'abc']
# aList.insert( 3, 2009)
# print "Final List : ", aList
# Final List : [123, 'xyz', 'zara', 2009, 'abc']  # 将L[3]挤到右边

# 测试用例:
# {67,0,24,58}
#
# 对应输出应该为:
# [58,24,0,67]