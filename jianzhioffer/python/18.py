#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/15


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root is not None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)