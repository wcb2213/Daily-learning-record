#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/25

'''optimize.root'''

import numpy as np
from scipy import optimize

# 1
func1 = lambda x: x + np.cos(x)
sol1 = optimize.root(func1, 0.3)# 0.3指算法迭代的初始值
print(sol1.x,sol1.fun)#解及对应的函数值

# 2 两元一次方程
func2 = lambda x: [x[0]*np.cos(x[1])-4, x[0]*x[1]-x[1]-5]
sol2 = optimize.root(func2, [1,1])
print(sol2.x,sol2.fun)
