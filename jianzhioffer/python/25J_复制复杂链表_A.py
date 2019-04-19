#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


# 25ms
# 复制复杂链表 新建链表 random不用新建
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        l_newlink = [] # 存储新链表每个节点的地址
        l_random = [] # 存储新链表每个节点的随机节点地址

        p = pHead  # 改变p的属性 pHead 也会变
        q = RandomListNode(p.label)
        while p:
            l_newlink.append(q)
            l_random.append(p.random) # 可能为 None
            if p.next:
                q.next = RandomListNode(p.next.label)
            p, q = p.next, q.next

        for i in range(len(l_newlink)):
            if l_random[i]:
                l_newlink[i].random = l_random[i]
        return l_newlink[0]