#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/22

import numpy as np
from scipy.stats import randint
import matplotlib.pyplot as plt


x = np.r_[0:7:8j]
# x = np.arange(8)
# x = np.array(range(0, 8))
print(randint(1, 7))
# plt.stem(x, randint(1, 7).pmf(x))
plt.stem(x, randint.pmf(x, 1, 7))#loc=2会左移两个单位
# randint.pmf 离散均匀分布
# randint.pmf(k) = 1./(high - low)
# for k = low, ..., high - 1.
# binom(n, p)二次分布
# poisson（mu）泊松分布 r'$exp(-mu)*k^mu/k!$'
plt.show()

# 自定义分布

# 假设检验