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

    # 已知前序和中序
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        pRoot = TreeNode(pre.pop)
        index = tin.index(pRoot.val)
        pRoot.left = self.reConstructBinaryTree(pre, tin[:index])
        pRoot.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return pRoot

    # 已知后序遍历与中序遍历
    def reConstructBinaryTree_post(self, post, tin):
        if not post or not tin:
            return None
        pRoot = TreeNode(post.pop)  #### 创建二叉树类
        index = tin.index(pRoot.val)
        pRoot.right = self.reConstructBinaryTree_post(post, tin[index+1:])
        pRoot.left = self.reConstructBinaryTree_post(post, tin[:index])
        return pRoot

if __name__ == '__main__':
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    post = [7,4,2,5,8,6,3,1]

    def tree_storeInList(p):
        if p == None:
            return []
        return [p.val] + tree_storeInList(p.left) + tree_storeInList(p.right) # 按照前序生成列表
        # return tree_storeInList(p.left) + [p.val] + tree_storeInList(p.right) # 按照中序生成列表
        # return tree_storeInList(p.left) + tree_storeInList(p.right) + [p.val] # 按照后序生成列表
    a = Solution()
    print(tree_storeInList(a.reConstructBinaryTree(pre, tin)))
    # print(tree_storeInList(a.reConstructBinaryTree_post(post, tin)))