#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/25

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def fly_dist(theta,v0):
    g = 9.8
    theta_rad = np.pi*theta/180
    return v0 ** 2/g * np.sin(2*theta_rad)
t = np.linspace(0,90)
plt.plot(t,fly_dist(t,1))
plt.xlabel(r'$\theta$')
plt.ylabel('d')
plt.show()# 看图大概是 45°最远

fly_dist_neg = lambda theta, v0: -fly_dist(theta, v0)
res = optimize.minimize(fly_dist_neg, 10, args=(1,))
print(res)
if res.success:
    print(r'$/theta$ = '+str(res.x))

## rosenbrock 测试优化算法效果的非凸函数
## 默认的优化算法 BFGS 还有 CG, Nelder-Mead