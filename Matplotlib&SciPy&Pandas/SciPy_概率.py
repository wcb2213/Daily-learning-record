#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/21

"""stats,norm"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-3, 3)
p = norm.pdf(x)#概率密度函数
p2 = norm.cdf(x)#累积分布函数
plt.plot(x, p,
         x, p2)
plt.show()
x_norm = norm.rvs(size=1000)
print(x_norm)