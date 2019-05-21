#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/21

"""interpolate.interp1d"""

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
t = np.linspace(0, 2*np.pi, 200)
f = interpolate.interp1d(x, y, kind='quadratic')# nearest zero linear quadratic cubic 4,5,6,7
# plt.plot(x, y)# 线条
# plt.plot(x, y, 'o')# 点
plt.plot(x, y, 'o',
         t, f(t))
plt.show()
