# -*- coding: utf-8 -*-


import math
# a = input('input:')
# l = list(map(int, a.split(' ')))
# input_list = [[l[0], l[1]], [l[2], l[3]], [l[4], l[5]], [l[6], l[7]], [l[8], l[9]]]

def mse(l1, l2):
    return math.sqrt(pow(l1[0]-l2[0], 2)+pow(l1[1]-l2[1], 2))

input_list = [[200, 0], [200, 10], [200, 50], [200, 30], [200, 25]]

l0, l1, l2, l3, l4, l5 = [], [], [], [], [], [] # 原点到5个点的mse距离，第一个点到5个点。。。
for i in range(5):
    l0.append(mse(input_list[i], [0, 0]))
for i in range(5):
    l1.append(mse(input_list[i], input_list[0]))
for i in range(5):
    l2.append(mse(input_list[i], input_list[1]))
for i in range(5):
    l3.append(mse(input_list[i], input_list[2]))
for i in range(5):
    l4.append(mse(input_list[i], input_list[3]))
for i in range(5):
    l5.append(mse(input_list[i], input_list[4]))

# res = []
# l12 = []
# for i in range(5):