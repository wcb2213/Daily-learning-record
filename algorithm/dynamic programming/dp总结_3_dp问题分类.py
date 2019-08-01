#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/7/31


#### 一、线性模型
# 1. 每段长度钢条对应价格（0，1，2，3。。。10） 求长度为10的钢条怎样切割价值最大
l = [0,1,5,8,9,10,17,17,20,24,30]
dp =[0]+[l[1]]
for i in range(2,11):
    m = 0
    for j in range(0,i):
        m = max(m,l[j]+l[i-j])
    dp.append(m)
print(dp)
# 2. 过河问题
# 四个人过桥花费的时间分别为 1 2 5 10 # 注意 不是贪婪算法哦
# 最多过两个人
# 第一步：1和2过去，花费时间2，然后1回来（花费时间1）；
# 第二歩：3和4过去，花费时间10，然后2回来（花费时间2）；
# 第三步：1和2过去，花费时间2，总耗时17。
# 将所有人按花费时间递增进行排序为 a:list
a = [0,1,2,5,10]
opt = [0]*len(a)
opt[1] = a[1]
opt[2] = a[2]
for i in range(3,5):
    opt[i] = min(opt[i-1]+a[1]+a[i] , opt[i-2]+a[1]+a[i]+2*a[2])#剩下一个人则 a[1]+a[i] 或者剩下两个人 最少的回来 剩下两人走 次少的回来 次少和最少的走
print(opt[-1])

#### 二、区间问题
# 1. 最少添加几个字符使得字符串变成回文串
## 递归
s = "abcb"
n = len(s)
dp = [[-1 for _ in range(n)] for _ in range(n)]
def dfs(i,j):
    if i>=j: return 0
    elif s[i]==s[j]: return dfs(i+1,j-1)
    else: return min(dfs(i+1,j), dfs(i,j-1))+1
for i in range(n):
    for j in range(n):
        dp[i][j]= dfs(i,j)
print(dp[0][n-1])
print(dp)
# 边界条件：无
# 转移方程：
# 当i>=k：q(i,j)=0
# 当s[i]==s[j]：q(i,j)=q(i+1,j-1)
# 当s[i]!=s[j]：q(i,kj)=min(dq(i+1,j), q(i,j-1))+1
## 备忘录dp
s = "abcb"
n = len(s)
dp = [[-1 for _ in range(n)] for _ in range(n)]
def dfs(i,j):
    if i>=j: return 0
    elif s[i]==s[j]: return dp[i+1][j-1] if dp[i+1][j-1]!=-1 else dfs(i+1,j-1)
    else: return min(dp[i+1][j] if dp[i+1][j]!=-1 else dfs(i+1,j), dp[i][j-1] if dp[i][j-1]!=-1 else dfs(i,j-1))+1
for i in range(n):
    for j in range(n):
        dp[i][j]= dfs(i,j)
print(dp[0][n-1])
print(dp)
## dp
s = "abcb"
n = len(s) #4
dp = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n-1,-1,-1):
    for j in range(n):
        if i>=j: dp[i][j]=0
        elif s[i]==s[j]: dp[i][j]=dp[i+1][j-1]
        else: dp[i][j] = min(dp[i+1][j], dp[i][j-1])+1
print(dp[0][n-1])
print(dp)

#### 三、背包问题