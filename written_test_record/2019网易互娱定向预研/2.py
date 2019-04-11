#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/11


# input
t = int(input())
lInput1, lN, lInput2 = [], [], []
for i in range(t):
    for j in range(8):
        lInput1.append(input())
    lN.append(int(input()))
    for k in range(lN[i]):
        s = input().split(' ')
        lInput2.append([int(s[0]), int(s[1]), int(s[2])])

# process
def process(lInput1, lInput2, n):
    # lChess为当前的棋子布局
    lChess = []
    for i in range(8):
        for j in range(8):
            if lInput1[i][j] == '*':
                lChess.append([i, j, 0])
            if lInput1[i][j] == 'o':
                lChess.append([i, j, 1])
    # 函数处理
    # 判断落子附近是否有异色的棋子，如有。
    # 横 竖 斜 三种情况，是否有同色棋子，然后之间是否全是异色棋子
    def func():
        pass
        return
    # 逐步处理
    for i in range(n):
        func(lChess, lInput2[i])
        lChess += lInput2[i]

for i in range(t):
    n = lN[i]
    process(lInput1[(i)*8:(1+i)*8], lInput2[0:n], n)
    lInput2 = lInput2[n:]