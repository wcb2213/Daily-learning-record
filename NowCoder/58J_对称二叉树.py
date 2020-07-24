#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/3


# 27ms
# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 没法直接递归，需要对左右子树进行递归
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def isSame(p, q):
            if p == None and q == None: return True
            if p == None or q == None: return False
            if p.val != q.val: return False
            return isSame(p.left, q.right) and isSame(p.right, q.left)

        return isSame(pRoot, pRoot)
