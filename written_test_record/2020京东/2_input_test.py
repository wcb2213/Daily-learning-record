#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/24


T = int(input())
n_list, m_list = [], []
matrix_list = []
for i in range(T):
    tmp_n, tmp_m = map(int, input().split(' '))
    n_list.append(tmp_n)
    m_list.append(tmp_m)
    for j in range(tmp_n):
        tmp_matrix = list(input())
        matrix_list.append(tmp_matrix)
for i in range(T):
    n = n_list[i]
    m = m_list[i]
    index1 = sum(m_list[0:i])
    list = matrix_list[index1:index1+m_list[i]]
    print(n,m,list)
    for i in range(n):
        if 'S' in list[i]:
            j = list[i].index('S')
            i += n
            j += m
            break
    print(i,j)

# n = 3
# m = 3
# list = [['s','#'],['#','.']]
# list = [['.','.','.'],['#','#','#'],['#','S','#']]