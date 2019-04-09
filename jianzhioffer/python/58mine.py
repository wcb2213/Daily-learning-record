#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/3


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 没法直接递归，需要对左右子树进行递归
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def compLandR(p1, p2):
            if not p1 and not p2:
                return True
            if (p1 and p2) and (p1.val == p2.val):
                return compLandR(p1.left, p2.right) and compLandR(p1.right, p2.left)
            # 从左右子树开始递归 00 01 10 11 四种情况需要重新判断
            return False

        if not pRoot:
            return True
        if (not pRoot.left and pRoot.right) or (pRoot.left and not pRoot.right):
            return False
        return compLandR(pRoot.left, pRoot.right)
