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
        if not root:
            return []
        res = [root.val]
        list_current = [root]
        while list_current:
            list_tmp = []
            for i in list_current:
                if i.left:
                    list_tmp.append(i.left)
                    res.append(i.left.val)
                if i.right:
                    list_tmp.append(i.right)
                    res.append(i.right.val)
            list_current = list_tmp
        return res