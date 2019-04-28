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
        p = pRoot
        if not p:
            return True
        return self.isSame(p.left,p.right)
    def isSame(self,p1,p2):
        if not p1 and not p2:
            return True
        if p1 and p2 and p1.val==p2.val:
            return self.isSame(p1.left,p2.right) and self.isSame(p1.right,p2.left)
        return False
