#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/25


# 50ms
# 由二叉树的前序遍历和中序遍历重建该二叉树
# 重建二叉树的过程即确定每个节点左右子节点

# 已知中序及任一其他序列，即可重建二叉树
# 必须得有中序遍历确定左右子树 节点前的序列为该节点的左子树；节点后的序列为右子树
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        flag = TreeNode(pre.pop(0))  #### 创建二叉树类
        index = tin.index(flag.val)
        flag.left = self.reConstructBinaryTree(pre, tin[:index])
        flag.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return flag

    # 已知后序遍历与中序遍历
    # # post[::-1] 即 上 右 左  跟 pre 左右相反
    # def reConstructBinaryTree(self, post, tin):
    #     ## post and tin
    #     if not post or not tin:
    #         return None
    #     flag = TreeNode(post.pop())  #### 创建二叉树类
    #     index = tin.index(flag.val)
    #     flag.right = self.reConstructBinaryTree(post(-1), tin[index+1:])
    #     flag.left = self.reConstructBinaryTree(post(-1), tin[:index])
    #     return flag