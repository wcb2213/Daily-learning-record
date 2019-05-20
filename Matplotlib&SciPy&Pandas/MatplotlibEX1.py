#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/20

"""实例：基于Matplotlib的三角函数可视化"""

import numpy as np
import matplotlib.pyplot as plt


# plt.xkcd()#漫画风格
x = np.linspace(-np.pi, np.pi)# num=50 默认，包含a,b
plt.plot(x, np.cos(x),
         x, np.sin(x))
# 1 得到Axes对象
ax = plt.gca()
# 2 设置坐标轴
ax.spines['right'].set_color('none')#将上轴设为透明
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')#将x轴设在下轴
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))#将下轴平移到y=0
ax.spines['left'].set_position(('data', 0))
# 3 设置刻度
# plt.xticks([-np.pi, -np.pi/2.0, 0, np.pi/2.0, np.pi])# 刻度（需为数组），label，字体大小是否倾斜等
plt.xticks([-np.pi, -np.pi/2.0, 0, np.pi/2.0, np.pi],
           ['$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$'])# 使用LaTex语法显示π而不是3.14
plt.yticks([-1, 0, 1])
# 4 添加图例
plt.legend(['cosine', 'sine'], loc='upper left', frameon=True)
# 5 添加第一象限交点
plt.text(np.pi/4-0.15, -0.17, '$\pi/4$')
plt.text(-0.6, np.cos(np.pi/4), '$\sqrt{2}/2$')
plt.plot([np.pi/4, np.pi/4], [0, np.cos(np.pi/4)], '--k')
plt.plot([0, np.pi/4], [np.cos(np.pi/4), np.cos(np.pi/4)], '--k')
# 6 上色
plt.fill_between(np.linspace(0, np.pi/4),
                 np.sin(np.linspace(0, np.pi/4)))
plt.fill_between(np.linspace(np.pi/4, np.pi/2),
                 np.cos(np.linspace(np.pi/4, np.pi/2)))
plt.show()