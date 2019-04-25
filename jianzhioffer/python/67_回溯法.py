#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/19


# 4 5
# . . # . #
# # . # . #
# # . # . #
# # . . . .
# n,m= map(int,input().split(' '))
# l = []
# for i in range(n):
#     l.append(input().split(' '))
# print(n,m,l)


def process(a,b,dict):
    r1=r2=r3=r4=False
    if a>0 and (a-1,b) not in dict and (l[a-1][b]=='.' or l[a-1][b]=='$'):
        if l[a-1][b]=='$' or (a-1==n-2 and b==m-1) or (a-1==n-2 and b==m-2):
            return True
        r1=process(a-1,b,dict+[(a-1,b)])

    if a<n-1 and (a+1,b) not in dict and (l[a+1][b]=='.' or l[a+1][b]=='$'):
        if l[a+1][b]=='$'or (a+1==n-2 and b==m-1) or (a+1==n-2 and b==m-2):
            return True
        r2=process(a+1,b,dict+[(a+1,b)])

    if b>0 and (a,b-1) not in dict and (l[a][b-1]=='.' or l[a][b-1]=='$'):
        if l[a][b-1]=='$'or (a==n-2 and b-1==m-1) or (a-1==n-2 and b-1==m-2):
            return True
        r3=process(a,b-1,dict+[(a,b-1)])

    if b<m-1 and (a,b+1) not in dict and (l[a][b+1]=='.' or l[a][b+1]=='$'):
        if l[a][b+1]=='$'or (a-1==n-2 and b+1==m-1) or (a-1==n-2 and b+1==m-2):
            return True
        r4=process(a,b+1,dict+[(a,b+1)])

    return r1 or r2 or r3 or r4
n,m=4,5
l =[['.', '.', '#', '.', '#'], ['#', '.', '#', '.', '#'], ['#', '.', '#', '.', '#'], ['#', '.', '.', '.', '.']]
dict=[(0,0)]
print(process(0,0,dict))