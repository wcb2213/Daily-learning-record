#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/15


# 源二叉树的镜像 （递归，每一步都是将当前节点的左右子树对换）
# 23ms
# 1 DFS（左右根）
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root: return None
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root

# 2 BFS
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root: return None
        l=[root]
        while l:
            pr=l.pop()
            pr.left,pr.right=pr.right,pr.left
            if pr.left: l.append(pr.left)
            if pr.right: l.append(pr.right)
        return root