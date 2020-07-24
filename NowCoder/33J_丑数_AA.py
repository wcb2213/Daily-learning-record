#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


# 27ms
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 每得到一个丑数，必然得到三个新的丑数（*2，*3，*5） 初始为[1]，然后做一个类似生成器的东西
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<0: return
        if index==0: return 0
        dp=[0]*(index+1)
        dp[1]=1
        a,b,c=1,1,1 #dp下标，从1开始
        for i in range(2,index+1):
            n2,n3,n5=dp[a]*2,dp[b]*3,dp[c]*5
            dp[i]=min(n2,n3,n5)
            if dp[i]==n2: a+=1 # 3个if去除重复
            if dp[i]==n3: b+=1
            if dp[i]==n5: c+=1
        return dp[index]

if __name__ == '__main__':
    a = Solution()
    print(a.GetUglyNumber_Solution(7))