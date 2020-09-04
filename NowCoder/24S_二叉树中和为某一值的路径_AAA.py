#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/18


# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 二叉树的路径及其变形问题 DFS
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#   方法1：解耦   DFS+路径存储
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
# 			class中的变量+self表示全局变量
# 			子函数可直接调用外部主体程序的可变变量，如list，此时list为全局变量
# 			函数与函数之间可通过传引用实现全局变量


# 			方法2：DFS和路径存储一起在recur中实现
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        def recur(root, num):
            if not root: return
            path.append(root.val)
            if not root.left and not root.right and root.val == num:
                res.append(path[:])##注意，这里传值
            recur(root.left, num - root.val)
            recur(root.right, num - root.val)
            path.pop() ##path在函数中改变了，整个递归需要回溯所以要抛出

        res, path = [], [] ## recur为子函数，故 res,path不用传引用或者+self
        recur(root, expectNumber)
        return res