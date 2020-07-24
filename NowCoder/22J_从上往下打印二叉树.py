#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/16

# 24ms
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 宽度优先遍历，不用递归用循环
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root: return []
        l=[root]
        res=[root.val]
        while l:
            p=l.pop(0)
            if p.left:
                l.append(p.left)
                res.append(p.left.val)
            if p.right:
                l.append(p.right)
                res.append(p.right.val)
        return res