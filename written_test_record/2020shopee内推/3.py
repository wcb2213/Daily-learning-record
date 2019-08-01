#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/14

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表没连接起来
node = list(map(int, input().split(' ')))
if not node:
    print()
else:
    tmp = node.pop(0)
    dict = {tmp:1}
    res = ListNode(tmp)
    p = res.next ## p = res
    for i in node:
        if i not in dict:
            p = ListNode(i) # p.next = ListNode(i)
            p = p.next
            dict[i] = 1
    print(res)