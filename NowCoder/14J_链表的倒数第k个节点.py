#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/5


# 链表的倒数第k个节点
# 降低空间复杂度

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        fa,sl=head,head
        for i in range(k):
            if fa==None: return
            fa=fa.next
        while fa:
            fa=fa.next
            sl=sl.next
        return sl