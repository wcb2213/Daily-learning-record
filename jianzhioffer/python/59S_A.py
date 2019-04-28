#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/28


# 24ms
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        p = pRoot
        if not p:
            return []
        l1 = [p]
        res = [[p.val]]
        a = 0
        while l1:
            l2,l3=[],[]
            a += 1
            for i in l1:
                if i.left:
                    l2.append(i.left)
                    l3.append(i.left.val)
                if i.right:
                    l2.append(i.right)
                    l3.append(i.right.val)
            l1 = l2
            if a%2==1:
                l3.reverse()
            if l3:
                res.append(l3)
        return res