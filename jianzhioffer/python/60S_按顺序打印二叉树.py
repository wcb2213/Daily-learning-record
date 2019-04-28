#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/3


# 25ms
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        p = pRoot
        if not p:
            return []
        res = [[p.val]]
        l = [p]
        while l:
            l2,l3 = [],[]
            for i in l:
                if i.left:
                    l2.append(i.left)
                    l3.append(i.left.val)
                if i.right:
                    l2.append(i.right)
                    l3.append(i.right.val)
            if l3:
                res.append(l3)
            l = l2
        return res