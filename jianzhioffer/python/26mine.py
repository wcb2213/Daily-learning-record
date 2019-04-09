#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        # l 存储的是链表的地址
        l = self.get_midOrderList(pRootOfTree)
        n = len(l)
        l[0].left = None
        for i in range(n-1):
            l[i].right = l[i+1]
            l[i+1].left = l[i]
        l[n-1].right = None
        return l[0]

    def get_midOrderList(self, t):
        res = []
        if t.left:
            res += self.get_midOrderList(t.left)
        res.append(t)
        if t.right:
            res += self.get_midOrderList(t.right)
        return res