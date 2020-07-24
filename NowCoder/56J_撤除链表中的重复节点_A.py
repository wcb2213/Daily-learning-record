#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


# 30ms
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 哈希
    def deleteDuplication(self, pHead):
        # write code here
        p=pHead
        if not p or not p.next: return p
        dic={}
        while p:
            if p.val not in dic: dic[p.val]=True
            else: dic[p.val]=False
            p=p.next
        res=ListNode(0)
        q,p=res,pHead
        while p:
            if dic[p.val]:
                q.next=p
                q=q.next
            p=p.next
        q.next=None
        return res.next
    # # 直接处理
    # def deleteDuplication(self, pHead):
    #     # write code here
    #     p = pHead
    #     if not p or not p.next: return p
    #     res = ListNode(0)
    #     q = res
    #     while p:
    #         if not p.next or p.val != p.next.val:
    #             q.next = p
    #             q = q.next
    #             p = p.next
    #         else:
    #             val=p.val
    #             while p.next and p.next.val==val:
    #                 p=p.next
    #             p = p.next
    #             if not p:
    #                 q.next=None
    #                 break
    #     return res.next