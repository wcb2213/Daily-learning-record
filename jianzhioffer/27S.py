#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


# 递归
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        # 递归 不分字母  所有排序一边
        self.perm(ss, res, '')
        res = list(set(res))
        # sorted 默认 升序
        return sorted(res)
    def perm(self, ss, res, path):
        if ss:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:], res, path+ss[i])
        else:
            res.append(path)

a = Solution()
print(a.Permutation('ABbA'))
# ['BAAb', 'AABb', 'bBAA', 'bABA', 'bAAB', 'BAbA', 'AbBA', 'BbAA', 'AbAB', 'ABAb', 'ABbA', 'AAbB'] 不用sorted
# ['AABb', 'AAbB', 'ABAb', 'ABbA', 'AbAB', 'AbBA', 'BAAb', 'BAbA', 'BbAA', 'bAAB', 'bABA', 'bBAA']