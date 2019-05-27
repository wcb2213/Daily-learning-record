#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/27

'''基于SciPy的主成分分析'''

import numpy as np
from scipy import linalg

# import pysnooper
#
# @pysnooper.snoop()
def pca(X,k):# 输入X为 n个d维数据
    m, s = X.mean(axis=0), X.std(axis=0)
    # print(m,s)
    # X_bar = (X-m) / s
    X_bar = (X - m)
    # print(X_bar)
    S = X_bar.T.dot(X_bar) / X.shape[0]
    # print(S)
    e, U = linalg.eig(S)# U中每一列为特征向量
    # print(e,U)
    Uk = U[:, :k]
    # print(Uk)
    Y = X_bar.dot(Uk)#其实为 Y.T
    # Y = Uk.T.dot(X_bar.T)
    return Y # 输出为5个1为数据


A7 = np.array([[-1,-1,0,2,0],
               [-2,0,0,1,1]])# 5个二维数据
# pca(A7.T, 1)
print(pca(A7.T, 2).T)#[[-2.12132034 -0.70710678  0.          2.12132034  0.70710678]]