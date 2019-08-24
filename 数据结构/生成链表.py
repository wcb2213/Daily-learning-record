#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/22

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
tmp1 = ListNode(2)
tmp1.next = head
tmp2 = ListNode(3)
tmp2.next = tmp1
head = tmp2
# head = {3, 2, 1}
# print(head.val)
# print(head.next.val)
# print(head.next.next.val)


def FindKthToTail(head, k):
    # write code here
    L = []
    while head is not None:
        L.append(head)
        head = head.next
    if len(L) < k or k < 1:
        return None
    return L[-k]

print(FindKthToTail(head, 1))