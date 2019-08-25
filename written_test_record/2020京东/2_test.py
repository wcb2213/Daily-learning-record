#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/8/24


n = 3
m = 3
# list = [['s','#'],['#','.']]
list = [['.','.','.'],['#','#','#'],['#','S','#']]
for i in range(n):
    if 'S' in list[i]:
        j = list[i].index('S')
        i += n
        j += m
        break
# print(i,j)

isTrue = 'No'
def search(i,j,dict):
    global isTrue
    if i != 0 and (i+1, j) not in dict and list[(i-1)%n][j%m]!='#':
        if list[(i-1)%n][j%m] == 'S':
            isTrue = 'Yes'
            return
        search(i-1,j,dict + [(i - 1, j)])
    if i != 3*n-1 and (i+1, j) not in dict and list[(i+1)%n][j%m]!='#':
        if list[(i+1)%n][j%m] == 'S':
            isTrue = True
            return
        search(i+1,j,dict + [(i+1, j)])
    if j != 0 and (i, j-1) not in dict and list[i%n][(j-1)%m]!='#':
        if list[i%n][(j-1)%m] == 'S':
            isTrue = True
            return
        search(i,j-1,dict + [(i, j-1)])
    if i != 3*m-1 and (i, j+1) not in dict and list[i%n][(j+1)%m]!='#':
        if list[i%n][(j+1)%m] == 'S':
            isTrue = True
            return
        search(i,j+1,dict + [(i, j+1)])
    return
search(i,j,[(i,j)])
print(isTrue)