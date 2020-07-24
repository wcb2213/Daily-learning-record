#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/8


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        p=pHead
        if not p: return None
        while p:
            tmp=RandomListNode(p.label)
            tmp.next=p.next
            p.next=tmp
            p=p.next.next
        p=pHead
        while p:
            p.next.random= None if p.random==None else p.random.next
            p=p.next.next
        p=pHead
        res=pHead.next
        while p:
            tmp=p.next
            p.next=p.next.next
            tmp.next= None if tmp.next==None else tmp.next.next
            p=p.next
        return res