#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/22

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,50)
y = 4*x+1.5
y_noise = y + np.random.randn(50)*2

# 一 多项式拟合(numpy)
# np.polyfit(x,y,n)
# coeff = np.polyfit(x,y_noise,1)
# f = np.poly1d(coeff)# 3.969 x + 1.14
f = np.poly1d(np.polyfit(x,y_noise,1))

# plt.plot(x,y_noise,'x',
#          x,coeff[0]*x+coeff[1])
plt.plot(x,y_noise,'x',
         x,f(x))
plt.legend(['data',
            '$n=1$'])
plt.axis([-6,6,-25,25])
plt.show()