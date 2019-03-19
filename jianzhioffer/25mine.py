#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


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
        # p = pHead 意味着 p变 则 pHead 也变
        p = pHead
        l_random = []
        # l_newlink 存的是从pHead链表地址的数组
        # RandomListNode(p.label) 即创建一个新链表， label=p.label 两个指针均为None
        l_newlink = [RandomListNode(p.label)]

        # newlink 是存储输出新链表的表头的数组，对应的p变也会导致数组元素的变化
        newlink = l_newlink[0]

        q = newlink
        while p:
            l_random.append(p.random)
            if p.next:
                # q 随时创建新链表节点
                q.next = RandomListNode(p.next.label)
                l_newlink.append(q.next)
            p, q = p.next, q.next
        for i in range(len(l_newlink)):
            if l_random[i]:
                l_newlink[i].random = l_random[i]
        return newlink