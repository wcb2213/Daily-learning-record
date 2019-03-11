#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/25


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        L = []
        while head is not None:
            L.append(head)  #### L中存储的是 head的 地址值 而不是 val
            head = head.next
        if len(L)<k or k<1:
            return None
        return L[-k]