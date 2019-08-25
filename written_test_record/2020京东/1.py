#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/24


## input
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

## process
for k in range(T):
    n = n_list[k]
    m = m_list[k]
    index1 = sum(m_list[0:k])
    list = matrix_list[index1:index1+m_list[k]]
    for i in range(n):
        if 'S' in list[i]:
            j = list[i].index('S')
            i += n
            j += m
            break

    isTrue = 'No'
    def search(i, j, dict):
        global isTrue
        if i != 0 and (i - 1, j) not in dict and list[(i - 1) % n][j % m] != '#':
            if list[(i - 1) % n][j % m] == 'S':
                isTrue = 'Yes'
                return
            search(i - 1, j, dict + [(i - 1, j)])
        if i != 3 * n - 1 and (i + 1, j) not in dict and list[(i + 1) % n][j % m] != '#':
            if list[(i + 1) % n][j % m] == 'S':
                isTrue = True
                return
            search(i + 1, j, dict + [(i + 1, j)])
        if j != 0 and (i, j - 1) not in dict and list[i % n][(j - 1) % m] != '#':
            if list[i % n][(j - 1) % m] == 'S':
                isTrue = True
                return
            search(i, j - 1, dict + [(i, j - 1)])
        if i != 3 * m - 1 and (i, j + 1) not in dict and list[i % n][(j + 1) % m] != '#':
            if list[i % n][(j + 1) % m] == 'S':
                isTrue = True
                return
            search(i, j + 1, dict + [(i, j + 1)])
        return

    search(i, j, [(i, j)])
    print(isTrue)