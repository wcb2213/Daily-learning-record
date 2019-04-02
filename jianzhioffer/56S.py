#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/2


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
        # q1 = res
        # q = pHead
        # while q:
        #     if l1.count(q.val) == 1:
        #         # q1.next = q # 不能用q 还是要新建链表值
        #         q1.next = ListNode(q.val)
        #         q1 = q1.next
        #     q = q.next
        return res.next


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