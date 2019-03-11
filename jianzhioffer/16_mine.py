#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/26


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(1)
        p = head
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next
            else:
                head.next = pHead1
                pHead1 = pHead1.next
            head = head.next
        if pHead1:
            head.next = pHead1
            pHead1 = None
        if pHead2:
            head.next = pHead2
            pHead2 = None
        return p.next