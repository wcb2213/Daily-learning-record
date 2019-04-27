#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


# 冒泡排序对n个数据操作n-1轮，每轮找出一个最大（小）值。
# 操作只对相邻两个数比较与交换，每轮会将一个最值交换到数据列首（尾），像冒泡一样。
def bubble(bubbleList):
    listLength = len(bubbleList)
    for i in range(listLength):
        for j in range(listLength-i-1):
            if bubbleList[j] > bubbleList[j + 1]:
                bubbleList[j], bubbleList[j + 1] = bubbleList[j + 1], bubbleList[j]
    print(bubbleList)

if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    bubble(bubbleList)