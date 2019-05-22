#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/22

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# 二 最小二乘优化进行拟合 scipy.optimize
def my_f(x,a,b,w,t):
    return a*np.exp(-b*np.sin(w*x+t))
x = np.linspace(0,2*np.pi)
actual_parameters = [3,2,1.25,np.pi/4]
y = my_f(x,*actual_parameters)
y_noise = y + 0.8*np.random.randn(len(y))
plt.plot(x,y,'x',
         x,y_noise)
plt.show()