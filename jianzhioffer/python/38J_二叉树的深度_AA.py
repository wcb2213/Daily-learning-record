#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/23


# 36ms
# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
# 注意在利用递归的时候怎么得到最大值
class Solution:
    def TreeDepth(self, pRoot):
        # write code here

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