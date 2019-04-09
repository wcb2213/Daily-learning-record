#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# Created by Vanish at 2019/2/24


# s1, s2 = [], []
# s2.append(1)
# s1.extend(s2)
# print(s1)
#
# s3 = s1 + s2
# print(s3)


# 创建二维数组
# a = [[6, 7, 8], [1, 2, 3, 4]] #### a的元素为数列 和矩阵不同
# matrix = [[0 for i in range(3)] for i in range(2)]
# print(matrix)

# print(a)
# print(len(a))
# print(a[0])
# print(a[1])

# a.reverse() ## 数列元素反向排列
# print(a)
# print(len(a))
# print(a[0])
# print(a[1])

# L = [] # 2 3 4
# L = [None] # 1 2 3 5
# if L: ## 数列是否有元素
#         #   注意 二维数组  L2=[[1]] pop后 L2=[]
#     print(1)
# if L is not None:  ##数列一定不为空
#     print(2)
# if L != None:
#     print(3)
# if not L:
#     print(4)
# while L:
#     print(5)
#     break
rows = 3
cols = 4
matrix = ['a','b','c','e','s','f','c','s','a','d','e','e']
matrix = [matrix[r*cols:(r+1)*cols] for r in range(0, rows)]
# matrix = [matrix[r:(r+1)] for r in range(0, rows)]
# board = [list(matrix[cols * i:cols * i + cols]) for i in range(rows)]
print(matrix)
arrive = [[0 for i in range(0, cols)] for i in range(0, rows)]
print(arrive)