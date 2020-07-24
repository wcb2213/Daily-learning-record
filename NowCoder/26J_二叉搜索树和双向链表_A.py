#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2020/7/8


# 大佬喝奶茶
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            # ifelse 执行第二个节点到最后，跳过第一个节点（最左边）并记录
            if self.pre:
                self.pre.right, cur.left = cur, self.pre
            else:
                self.head = cur
            self.pre = cur #不断赋值，循环完毕后为最后一个节点（最右边）
            dfs(cur.right)

        p = pRootOfTree
        if not p: return
        self.pre = None #跳过第一个的左和最后一个的右
        #self.head = None #只是变量声明，由于是全局变量，可省略
        dfs(p)
        # self.head.left, self.pre.right = self.pre, self.head #循环双向链表
        self.head.left = None
        self.pre.right = None
        return self.head