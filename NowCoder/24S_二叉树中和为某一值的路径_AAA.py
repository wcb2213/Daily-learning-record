#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/18


# 运行时间：31ms
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 二叉树的路径及其变形问题 DFS
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root: return []
        self.num = expectNumber ## FindPath，DFS为两个函数，定义变量时+self即成为全局变量，
        res = [] ## res可直接传引用或者加self成为全局变量
        self.DFS(root,res,[root.val])
        return res
    def DFS(self,root,res,path):
        if not root.left and not root.right and sum(path)==self.num:
            res.append(path)
        ##path在函数中没有改变，可以认为传值而不用抛出
        if root.left:
            self.DFS(root.left, res,path+[root.left.val])
        if root.right:
            self.DFS(root.right, res,path+[root.right.val])