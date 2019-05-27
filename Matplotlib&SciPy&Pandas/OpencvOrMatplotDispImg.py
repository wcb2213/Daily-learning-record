#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2018/8/21

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# grayImg = cv.imread('1.jpg',cv.IMREAD_GRAYSCALE)
# cv.imwrite('mygray.jpg',grayImg)
# cv.imshow('grayImg',grayImg)
# cv.waitKey(0)
# cv.destoryAllWindows()

img1 = cv.imread('1.jpg', cv.IMREAD_GRAYSCALE)
# img2 = cv.imread('楚门的世界3.jpg', cv.IMREAD_COLOR) # 报错 不识别中文
img2 = cv.imread('2.jpg', cv.IMREAD_COLOR)

img1 = cv.cvtColor(img1, cv.COLOR_GRAY2RGB)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.show()
