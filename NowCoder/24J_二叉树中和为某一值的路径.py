#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/6


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