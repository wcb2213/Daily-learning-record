#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


# 36ms
# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# 注意在利用递归的时候怎么得到最大值
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        # level仅在函数参数和return中，不用处理
        # maxlevel在函数中有赋值处理，需要考虑是否回溯
        def recur(root, level):
            maxlevel = level
            if root.left != None:
                maxlevel = max(maxlevel, recur(root.left, level + 1))
            if root.right != None:
                maxlevel = max(maxlevel, recur(root.right, level + 1))
            return maxlevel

        if pRoot == None:
            return 0
        return recur(pRoot, 1)

    ## 简化
    ## 递归中TrueFalse或者一个数字  这类输出一个结果的 在return实现可以简洁代码
    # def TreeDepth(self, pRoot):
    #     # write code here
    #     if not pRoot:
    #         return 0
    #     return 1+max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))