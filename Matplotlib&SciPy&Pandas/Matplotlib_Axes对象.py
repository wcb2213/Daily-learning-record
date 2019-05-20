#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/20

"""基于对象的可视化操作"""

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)#构建数组，类似range
t2 = np.arange(0.0, 5.0, 0.02)

#### 一

plt.subplot(211)
plt.plot(t1, f(t1), 'bo',
         t2, f(t2), 'k')
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()

#### 二 基于对象
fig, axes = plt.subplots(2, 1)
axes[0].plot(t1, f(t1), 'bo',
             t2, f(t2), 'k')
axes[1].plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()