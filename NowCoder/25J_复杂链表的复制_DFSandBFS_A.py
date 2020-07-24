#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


# 25ms
# 复杂链表的复制
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
## 哈希
# 1 递归 DFS
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        def dfs(p): # 1234构成DFS
            if not p: return None #1
            if p in visited: return visited[p]
            copy = RandomListNode(p.label) #2
            visited[p] = copy
            copy.next = dfs(p.next) #3
            copy.random = dfs(p.random) #4
            return copy

        p = pHead
        visited = {}
        return dfs(p)
# 2 非递归 BFS
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        def bfs(p):
            if not p: return None
            l = [p]
            visited[p] = RandomListNode(p.label)
            while l:
                tmp = l.pop(0)
                if tmp.next and tmp.next not in visited:
                    l.append(tmp.next)
                    visited[tmp.next] = RandomListNode(tmp.next.label)
                if tmp.random and tmp.random not in visited:
                    l.append(tmp.random)
                    visited[tmp.random] = RandomListNode(tmp.random.label)
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return visited[p]

        p = pHead
        visited = {}
        return bfs(p)