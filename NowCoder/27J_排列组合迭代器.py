#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/19


import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss: return []
        # 得到排列组合的迭代器，元素样式为（a,a,c）tuple, 并且注意是有序的，这个有序指字符串的顺序
        res=itertools.permutations(ss)
        dic={}
        result=[]
        for i in res:
            if i not in dic:
                dic[i]=True
                result.append(''.join(i))
        return result

    # def Permutation(self, ss):
    #     # write code here
    #     return [] if not ss else sorted(list(set(map(lambda s:''.join(s), itertools.permutations(ss)))))