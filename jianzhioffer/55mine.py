#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        l1, l2 = [], []
        p = pHead
        while p:
            l1.append(p)
            if p.val in l2:
                return l1[l2.index(p.val)]
            l2.append(p.val)
            p = p.next
        return None