#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/25


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        flag = TreeNode(pre.pop(0))  #### 创建二叉树类
        index = tin.index(flag.val)
        flag.left = self.reConstructBinaryTree(pre, tin[:index])  #### 为什么 有 pre
        flag.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return flag