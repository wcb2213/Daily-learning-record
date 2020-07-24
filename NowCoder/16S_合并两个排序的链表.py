#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/26


# 47ms
# 时间复杂度：O(m+n),m，n分别为两个单链表的长度
# 空间复杂度：O(1)
# 合并两个排序的链表
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
        if pHead1!=None:
            p.next=pHead1
        if pHead2!=None:
            p.next=pHead2
        return head.next