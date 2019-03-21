#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i + 1]:
                bubbleList[i], bubbleList[i + 1] = bubbleList[i + 1], bubbleList[i]
        listLength -= 1
    print(bubbleList)

print(__name__)
if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    bubble(bubbleList)