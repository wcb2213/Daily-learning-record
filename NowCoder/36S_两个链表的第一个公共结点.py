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
        p1,p2=pHead1,pHead2
        while p1!=p2:
            p1=p1.next if p1 else pHead2
            p2=p2.next if p2 else pHead1
            # 不用下面这个，因为可能不存在公共节点，需要None
            # p1 = p1.next if p1.next else pHead2
        return p1