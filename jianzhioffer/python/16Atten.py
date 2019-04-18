#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/26


# 47ms
# 合成链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(1) # 任意值均可
        p = head
        while pHead1 and pHead2:
            if pHead1.val > pHead2.val:
                p.next = pHead2
                pHead2 = pHead2.next
            else:
                p.next = pHead1
                pHead1 = pHead1.next
            p = p.next
        while pHead1:
            p.next = pHead1
            pHead1 = pHead1.next
            p = p.next
        while pHead2:
            p.next = pHead2
            pHead2 = pHead2.next
            p = p.next
        return head.next