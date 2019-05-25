#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/25

'''scipy.intergrate'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import special,integrate

# 1 import sympy : 可实现符号变量显示，定积分，多元函数积分

# 2 数值积分
f = lambda x: special.jv(2.5,x)
x = np.linspace(0,10)
plt.plot(x,f(x))
plt.show()
# 2.1 函数积分法
value , max_err = integrate.quad(f,0,10)#计算f在[0,10]的积分，value为积分得到的值，max_err为积分结果的最大误差
# g = lambda x: np.exp(-x**0.5)
# value , max_err = integrate.quad(g,0,np.inf)#计算g,[0,正无穷）

#双重积分
h = lambda x, t, n: np.exp(-x*t) / (t**n) # 积分结果为 1/n
i_n = lambda n: integrate.dblquad(h,
                                  1, np.inf,# 对x积分
                                  lambda t: 0, lambda t: np.inf,# 对 t积分
                                  args=(n,))[0] # integrate.dblquad 输出 value , max_err
for i in [1,2,3,4]:
    print(i_n(i), end=' ')
print()

# 2.2 采样点积分法（用于估算积分）
x = np.linspace(0,np.pi,100)#采样点越多，越准确
y = np.sin(x)#积分值为2
print(integrate.simps(y,x), integrate.trapz(y,x))
