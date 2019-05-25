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

# 1 定义误差函数
def err_f(p,x,y):
    return y-my_f(x,*p)
## 相当于已知输入 x（准确），输出y_noise(不准确),作用函数f,参数缺失，求得最合适的参数
c, rv = optimize.leastsq(err_f,[1,1,1,1],args=(x,y_noise))
print(c, rv)# rv 为1~4中的某个值， c为得到的参数
# 2 不定义误差函数直接拟合
p_est, err_est = optimize.curve_fit(my_f,x,y_noise)
print(p_est, err_est)# p_est为估计的参数 err_est为估计的参数的四个协方差矩阵

plt.plot(x,y,'rx',
         x,y_noise,'b--',
         x,my_f(x,c[0],c[1],c[2],c[3]),'k:')
plt.show()