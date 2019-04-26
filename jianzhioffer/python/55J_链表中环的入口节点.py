#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


# 27ms
# 链表中环的入口节点
# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        dict = []
        p = pHead
        while p:
            if p in dict:
                return p
            dict.append(p)
            p = p.next