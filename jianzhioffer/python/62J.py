#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 中序 左根右 递归
class Solution:
    # 同 res = [] 不一样的
    def __init__(self):
        self.res = []
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.midRecur(pRoot)
        if k <= 0 or (k > len(self.res)):
            return None
        return self.res[k-1]

    def midRecur(self, p):
        if not p:
            return None
        self.midRecur(p.left)
        self.res.append(p)
        self.midRecur(p.right)