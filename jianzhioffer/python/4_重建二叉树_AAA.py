#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/2/25


# 50ms
# 由二叉树的前序遍历和中序遍历重建该二叉树
# 重建二叉树的过程即确定每个节点左右子节点

# 前序：根 左子树 右子树
# 中序：左子树 根 右子树
# 后序：左子树 右子树 根
# 已知中序和另一个序列，即可重建
# 已知前序加后序，可重建不唯一的二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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

    # # 已知后序遍历与中序遍历
    # def reConstructBinaryTree(self, post, tin):
    #     ## post and tin
    #     post = post[::-1] # post[::-1] 即 上 右 左  跟 pre 左右相反
    #
    #     def recur(post, tin):
    #         if not post or not tin:
    #             return None
    #         flag = TreeNode(post.pop(0))  #### 创建二叉树类
    #         index = tin.index(flag.val)
    #         flag.right = recur(post, tin[index+1:])
    #         flag.left = recur(post, tin[:index])
    #         return flag
    #
    #     return recur(post, tin)

if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    post = [7,4,2,5,8,6,3,1]

    # def tree_pre_print(p):
    #     if p == None:
    #         return
    #     print(p.val)
    #     tree_pre_print(p.left)
    #     tree_pre_print(p.right)
    def tree_storeInList(p):
        if p == None:
            return []
        return [p.val] + tree_storeInList(p.left) + tree_storeInList(p.right) # [1, 2, 4, 7, 3, 5, 6, 8]
        # return tree_storeInList(p.left)+ [p.val] + tree_storeInList(p.right) # [4, 7, 2, 1, 5, 3, 8, 6]
    a = Solution()
    # tree_pre_print(a.reConstructBinaryTree(pre, tin)) # 1 2 4 7 3 5 6 8
    # tree_pre_print(a.reConstructBinaryTree(post, tin)) # 1 2 4 7 3 5 6 8
    print(tree_storeInList(a.reConstructBinaryTree(pre, tin)))