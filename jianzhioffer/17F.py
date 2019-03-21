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
            # 如果结点相等，Subtree函数负责判断
            # 这两个结点的孩子是否相等
            res = Solution.Subtree(self, pRoot1, pRoot2)
        if not res:
            # 当与小树相同的子树不在根部，找大树左子树
            res = Solution.HasSubtree(self, pRoot1.left, pRoot2)
        if not res:
            # 左边找到了就不需要再找了
            res = Solution.HasSubtree(self, pRoot1.right, pRoot2)
        return res

    def Subtree(self, pRoot1, pRoot2):
        # 下面两个if位置不能反
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        # 左右同时相等时
        return Solution.Subtree(self, pRoot1.left, pRoot2.left) and \
               Solution.Subtree(self, pRoot1.right, pRoot2.right)