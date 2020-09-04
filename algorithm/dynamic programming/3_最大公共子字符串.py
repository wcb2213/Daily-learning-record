#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/23


# 最长公共子序列
def find_long_com_substr(s1, s2):
    m=[[0 for _ in range(len(s2)+1)]  for _ in range(len(s1)+1)]  
    cnt=0   #最长匹配的长度
    idx=0  #最长匹配对应在s1中的最后一位
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                tmp=m[i-1][j-1]+1
                m[i][j]=tmp
                if tmp>cnt:
                    cnt=tmp
                    idx=i
    return s1[idx-cnt:idx],cnt   #返回最长子串及其长度

# 最小编辑距离
def min_edit_distance(ss1,ss2):
    dp=[[0]*(len(ss2)+1) for _ in range(len(ss1)+1)]
    for i in range(1,len(ss1)+1):
        dp[i][0]=i
    for j in range(1,len(ss2)+1):
        dp[0][j]=j
    for i in range(1,len(ss1)+1):
        for j in range(1,len(ss2)+1):
            if ss1[i-1]==ss2[j-1]: cost=0
            else: cost=1
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+cost)
    return dp[i][j]

if __name__=="__main__":
    s1,s2="abcde",'aebcdf'
    ss1,ss2="batyu","beauty"
    print(find_long_com_substr(s1,s2))
    print(min_edit_distance(ss1,ss2))