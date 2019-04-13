#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/13


# input
n = int(input())
l_input = []
for i in range(n-1):
    l_input.append(input().split(' '))
print(l_input)

# process
# def f1 输入： l 为连接关系， s2为s的连接通道
def f1(s, l):
    if l[0] == s:
        s2 = l[1]
    else:
        s2 = l[0]
    return s2
# def process 输入1的子通道 计算该子通道广度
def process(sub_chan):
    global t
    for i in range(n-1):
        if i not in dict and sub_chan in l_input[i]:
            t += 1
            s = f1(sub_chan, l_input[i])
            dict.add(i)
            process(s)
    return

dict = {-1} # 记录已使用的关系
l1_line = [] # 1 的子通道
for i in range(n-1):
    if '1' in l_input[i]:
        s = f1('1', l_input[i])
        dict.add(i)
        l1_line.append(s)
# print(l1_line, dict)

# 计算疏散时间
time = []
for i in l1_line:
    t = 0 #1的每个子通道的疏散时间
    process(i)
    time.append(t)

print(max(time)+1)#子通道到通道1 再加1