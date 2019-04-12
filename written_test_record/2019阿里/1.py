#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/12


# n = 3
# lInput = [0.8, 0.7, 0.6]

# input
n = int(input())
lInput = []
for i in range(n):
    lInput.append(float(input()))

# process
a = (len(lInput)+99)//(len(lInput))
l = lInput*a
l = l[0:100]# l为100轮每轮的概率

p = []# p为1-100轮小明获胜的概率
i = 0
def process(p1):# p1为之前没有人获胜的概率，p2为当前有人获胜的概率
    global i
    if i <= 99:
        p2 = l[i]
        i += 1
        p.append(p1*p2)
        process(p1*(1-p2))
    return

# main
process(1)
print('%0.4f' % sum(p[::2]))