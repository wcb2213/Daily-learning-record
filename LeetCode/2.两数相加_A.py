#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/10


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(1)
        p = res
        flag = 0
        while l1 or l2:
            # 要用这个判断 首先 l1 得存在
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tmp = x+y+flag
            # 11//10=1  11/10=1.1
            flag = tmp//10
            p.next = ListNode(tmp%10)
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 判断最高位相加是否有进位
        if flag == 1:
            p.next = ListNode(1)
        return res.next