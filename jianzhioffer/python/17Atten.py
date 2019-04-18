#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/15


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if pRoot1 == None or pRoot2 == None:
            # 根据题干要求返回False
            return res
        if pRoot1.val == pRoot2.val:
            res = Solution.Subtree(self, pRoot1, pRoot2)
        if not res:
            res = Solution.HasSubtree(self, pRoot1.left, pRoot2)
        if not res:
            res = Solution.HasSubtree(self, pRoot1.right, pRoot2)
        return res

    def Subtree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return Solution.Subtree(self, pRoot1.left, pRoot2.left) and \
               Solution.Subtree(self, pRoot1.right, pRoot2.right)