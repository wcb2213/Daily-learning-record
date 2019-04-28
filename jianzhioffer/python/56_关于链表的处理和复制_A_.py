#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


# 这个是错的  因为没有考虑两个相同节点相邻的情况
# 还是使用list 重新创建 一个链表的好
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 链表 p = p.next， 跳出一个链表值后，q.next.next 之类会改变。
# 因而将链表地址存储在list中
# 注意链表地址和链表值的区别
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
            q.next = None

if __name__ == '__main__':
    q = ListNode(1)
    q.next = ListNode(2)
    q.next.next = ListNode(3)
    q.next.next.next = ListNode(3)
    q.next.next.next.next = ListNode(4)
    q.next.next.next.next.next = ListNode(4)
    q.next.next.next.next.next.next = ListNode(5)
    a = Solution()
    p = a.deleteDuplication(q)
    while p:
        print(p.val)
        p = p.next
