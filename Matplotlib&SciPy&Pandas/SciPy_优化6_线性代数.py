#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/27

'''scipy.linalg'''

import numpy as np
from scipy import linalg

A = np.mat('[1,2;3,4]')
# A = np.array([[1,2],
#               [3,4]])
# print(A)

## 一 基本操作
# 1 转置
A.T
# 2 逆矩阵
A.I
linalg.inv(A) # 用于求不可逆矩阵的逆矩阵
# 3 矩阵乘法
# print(A.dot(linalg.inv(A)))

## 二 线性方程组的求解
A2 = np.array([[1,3,5],
               [2,5,-1],
               [2,3,8]])
b = np.array([10,8,3])
# print(linalg.inv(A2).dot(b))
# print(linalg.solve(A2,b))# 效率更高

## 三 行列式的计算
linalg.det(A)

## 四 矩阵和向量的范数
linalg.norm(A)# 默认 'fro' 所有元素的平方和再开根号
linalg.norm(A,1)# 列范数 矩阵中每列元素之和中的最大值  向量所有元素绝对值的和
linalg.norm(A,np.inf)# 行范数 。。。  向量即所有元素绝对值的最大值
linalg.norm(A,2) # 2范数 矩阵的最大奇异值 向量即便为'fro'
linalg.norm(b,0) # 0范数 向量中0的个数
# print(linalg.norm(np.array([1,2,3,-4]),np.inf))

## 五 广义逆 针对不是方阵的矩阵
A5 = np.array([[1,2,3],
               [4,5,6]])
# print(linalg.pinv(A5))

## 六 特征值与特征向量
A6 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
l, v = linalg.eig(A6)
# print(l, v)
np.allclose(A6.dot(l), l * v)

## 七 奇异值分解
print('----------------7--------------')
A7 = np.array([[-1,-1,0,2,0],
               [-2,0,0,1,1]])
U, s, Vh = linalg.svd(A7)# 注意s为所有奇异值的一维数组
print('U, s, Vh', U, s, Vh)
S = linalg.diagsvd(s,2,5)# 将s变为M*N的S矩阵
# print('S',S)
np.allclose(A7, U.dot(S.dot(Vh)))# 验证奇异值分解
# print(U.dot(S.dot(Vh)))
# print(np.allclose(A7, U.dot(S.dot(Vh))))
# U_reduce = np.array([U[0][0:2],
#                      U[1][0:2],
#                      U[2][0:2]])
U_reduce = U[:, :2]
# print('U_reduce:',U_reduce)
# print('U_reduceT*A7',U_reduce.T.dot(A7))# k=1 [[-2.12132034 -0.70710678  0.          2.12132034  0.70710678]]
## 左奇异矩阵可以用于行数的压缩,右奇异矩阵可以用于列数即特征维度的压缩
