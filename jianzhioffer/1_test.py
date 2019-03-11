#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/12/13

####    显示多维数组的每一行
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15], [], [1]]

#   方法一
for iterm in array:
    print(iterm)
    # [1, 2, 8, 9]
    # [2, 4, 9, 12]
    # [4, 7, 10, 13]
    # [6, 8, 11, 15]
    # []
    # [1]

#   方法二（这个更好？）
n = len(array)
for i in range(n):
    print(array[i])