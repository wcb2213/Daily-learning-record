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
    def deleteDuplication(self, pHead):
        # write code here
        q = pHead
        l1 = []
        while q:
            l1.append(q.val)
            q = q.next
        res = ListNode(None)
        q = res
        for i in l1:
            if l1.count(i) == 1:
                q.next = ListNode(i)
                q = q.next
        return res.next