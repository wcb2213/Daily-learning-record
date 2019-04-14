#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/14


# 没做完
# input
# 1
# 8
# 2 1 1 2 2
# 2 1 1 1 4
# 2 1 1 2 2
# 2 2 2 1 4
# 0
# 0
# 1 1 1
# 1 1 1
# output
# 3
# input
t = 1
n = 8
# l_input = [[2,1,1,2,2],[2,1,1,1,4],[2,1,1,2,2],[2,2,2,1,4],[0],[0],[1,1,1],[1,1,1]]
eigNPerFrame = [2, 2, 2, 2, 0, 0, 1, 1]
eig_l = [['1', '1', '2', '2'], ['1', '1', '1', '4'], ['1', '1', '2', '2'], ['2', '2', '1', '4'], [], [], ['1', '1'], ['1', '1']]

# process
def find_lcsubstr(s1, s2):
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax=0   #最长匹配的长度
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
    return mmax   #返回最长子串及其长度

## 怎么分成16个字符串呢
def recur(n, l):
    for i in range(n):
        recur


