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
# 1. 部分背包问题（可以只取物品的一部分放入背包）
#     采用直观的贪心策略：优先放入''价量比''（价值除以质量）最大的，直到背包不能再放入（或物品已取完）。
# 2. 01 背包问题(每个物品只有两种情况 “放” 或 “不放”)
v = [0,60, 100, 120]
w = [0,10, 20, 30]
bagWeight = 50
dp = [[0 for _ in range(bagWeight+1)] for _ in range(len(v))]
def dfs(i,j):
    if i==0 or j==0: return 0
    elif w[i]>j: return dfs(i-1,j)
    else: return max(dfs(i-1,j-w[i])+v[i],dfs(i-1,j))
for i in range(1,len(v)):
    for j in range(1,bagWeight+1):
        dp[i][j]=dfs(i,j)
print(dp)
print(dp[-1][-1])
# 转移方程：
# 当j<w[i]：dp[i][j] = dp[i-1][j]
# 当j>=w[i]：dp[i][j] = max(dp[i-1][j-w[i]],dp[i-1][j]) 可以装下时，可选拿或不拿
v = [0, 60, 100, 120]
w = [0, 10, 20, 30]
bagWeight = 50
dp = [[0 for _ in range(bagWeight + 1)] for _ in range(len(v))]
for i in range(1, len(v)):
    for j in range(1, bagWeight + 1):
        if w[i] <= j:
            dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp)
## 优化空间复杂度
v = [0,60,100,120]
w = [0,10,20,30]
bagWeight = 50
dp = [0 for _ in range(bagWeight+1)]
for i in range(1,len(v)):
    for j in range(bagWeight,0,-1):
        if w[i]<=j:
            dp[j] = max(dp[j-w[i]]+v[i], dp[j])
print(dp)
print(dp[-1])
## 01背包的满包问题
v = [0, 60, 100, 120]
w = [0, 10, 20, 30]
bagWeight = 50
dp = [[float("-inf") for _ in range(bagWeight + 1)] for _ in range(len(v))]
for i in range(1, len(v)):
    for j in range(1, bagWeight + 1):
        if w[i] < j:
            dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
        elif w[i] == j:
            dp[i][j] = max(v[i], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp)
## 背包问题的路径记录
# 递归
n,m=3,50
res = []
def recur(i,j):
    if i==0: return
    if dp[i][j] == dp[i-1][j]:
        res.append(i)
        return recur(i-1,j-w[i])
    return recur(i-1,j)
recur(n,m)
print(res)
# 循环
n,m=3,50
res = []
for i in range(n,0,-1):
    if dp[i][m]==dp[i-1][m]:
        res.append(i)
        m -= w[i]
print(res)
# 3.完全背包问题（同一物品有无穷件）
# 4.多重背包（同一物品有多件）