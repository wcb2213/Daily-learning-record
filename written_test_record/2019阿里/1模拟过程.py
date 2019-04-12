#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/12


# 这个程序首先会随机产生若干0~1之间的实数{p_1, p_2, …, p_n}，
# 然后从小明开始，第一轮以p_1的概率将奖金全部分配给小明，第二轮以p_2的概率将奖金全部分配给小华，
# 这样交替地小明、小华以p_i的概率获得奖金的全部，一旦奖金被分配，则程序终止，如果n轮之后奖金依旧没发出，
# 则从p_1开始继续重复（这里需要注意，如果n是奇数，则第二次从p_1开始的时候，这一轮是以p_1的概率分配给小华）；
# 直到100轮，如果奖金还未被分配，程序终止，两人约定通过支付宝将奖金捐出去。

# 输入:
# 输入数据包含N+1行，
# 第一行包含一个整数N
# 接下来N行，每行一个0~1之间的实数，从p_1到p_N
# 输出:
# 单独一行，输出一个小数，表示小明最终获得奖金的概率，结果四舍五入，小数点后严格保留4位(这里需要注意，如果结果为0.5，则输出0.5000)。
# 输入范例:
# 1
# 0.999999
# 输出范例:
# 1.0000


import random
# input
n = int(input())
lInput = []
for i in range(n):
    lInput.append(float(input()))


# 模拟了这个过程
res = []
num = 0
for j in range((n+99)//n):  # 经过大于等于100轮
    for i in range(n):
        randN = random.random()# 产生0到1的随机数
        num += 1
        if randN <= lInput[i]:
            res.append(num)  # 记录成功时的num值
if len(res):
    if res[0] >= 100:
        print(0)  # 捐给支付宝
    else:
        print(res[0]%2)  # 1为小明 2为小华
else:
    print(0)  # 捐给支付宝