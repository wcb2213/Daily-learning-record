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
        if not pHead.next or not pHead.next.next: return None
        fa,lo=pHead.next.next,pHead.next
        while lo!=fa:
            if not fa.next or not fa.next.next: return None
            fa=fa.next.next
            lo=lo.next
        fa=pHead
        while fa!=lo:
            fa=fa.next
            lo=lo.next
        return fa

    # def EntryNodeOfLoop(self, pHead):
    #     # write code here
    #     p=pHead
    #     dic={}
    #     while p:
    #         if p in dic: return p
    #         else: dic[p]=1
    #         p=p.next
    #     return None
