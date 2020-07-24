#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/3


# 25ms
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        p=pRoot
        if not p: return []
        res=[]
        queue=[p]
        while queue:
            row=[]
            for i in queue:
                row.append(i.val)
            res.append(row)
            tmp=[]
            for i in queue:
                if i.left: tmp.append(i.left)
                if i.right: tmp.append(i.right)
            queue = tmp
        return res