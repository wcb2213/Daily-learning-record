#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/4



#  1. 对于序列化：使用前序遍历，递归的将二叉树的值转化为字符，并且在每次二叉树的结点
# 不为空时，在转化val所得的字符之后添加一个' ， '作为分割。对于空节点则以 '#' 代替。
#  2. 对于反序列化：按照前序顺序，递归的使用字符串中的字符创建一个二叉树(特别注意：
# 在递归时，递归函数的参数一定要是char ** ，这样才能保证每次递归后指向字符串的指针会
# 随着递归的进行而移动！！！)
#   这还只是前序
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    flag = -1

    def Serialize(self, root):
        if not root:
            return '$,'
        s = str(root.val) + ','
        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        s += left + right
        return s

    def Deserialize(self,s):
        l = s.split(',')
        return self.recursion1(l)

    def recursion1(self, l):
        self.flag += 1
        root = None
        if l[self.flag] != '$':
            root = TreeNode(int(l[self.flag]))
            root.left = self.recursion1(l)
            root.right = self.recursion1(l)
        return root