#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/24


input_list = []
for i in range(5):
    tmp = list(map(int, input().split(' ')))
    input_list.append(tmp)
# print(input_list)

number = []
for i in range(1,4):
    tmp = 0
    for j in range(0,5):
        tmp += input_list[j].count(i)
    number.append(tmp)
# print(number)
big_number = max(number)
big_number_index = number.index(big_number)+1
# print(big_number_index)

total = big_number
for i in range(1,4):
    if i != big_number_index:
        pass
