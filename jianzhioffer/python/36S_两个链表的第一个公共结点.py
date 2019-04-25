#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


# 24ms
# 输入两个链表，找出它们的第一个公共结点。
# 公共节点具有相同的地址
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        p1 = pHead1
        p2 = pHead2
        if not p1 or not p2:
            return
        while p1:
            list1.append(p1)
            p1 = p1.next
        while p2:
            if p2 in list1:
                return p2
            else:
                p2 = p2.next