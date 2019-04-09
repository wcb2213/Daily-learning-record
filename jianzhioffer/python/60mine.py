#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/3


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        stack = [pRoot]
        while stack:
            rs = []
            ns = []
            for i in stack:
                rs.append(i.val)
                if i.left:
                    ns.append(i.left)
                if i.right:
                    ns.append(i.right)
            res.append(rs)
            stack = ns
        return res