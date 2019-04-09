#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 错误答案，链表 p = p.next， 跳出一个链表值后，q.next.next 之类会改变。 最好新写一个链表
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        l1, l2 = [], []
        p = pHead
        while p:
            l1.append(p)
            if p.val in l2:
                q = l1[-2]
                self.jumpjump(q)
                index = l2.index(p.val)
                q = l1[index-1]
                self.jumpjump(q)
            l2.append(p.val)
            p = p.next
        return pHead

    def jumpjump(self, q):
        if q.next.next:
            q.next = q.next.next
        else:
            q.next.next = None

if __name__ == '__main__':
    q = ListNode(1)
    q.next = ListNode(2)
    q.next.next = ListNode(3)
    q.next.next.next = ListNode(3)
    q.next.next.next.next = ListNode(4)
    a = Solution()
    p = a.deleteDuplication(q)
    while p:
        print(p.val)
        p = p.next
