#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


"""冒泡排序"""
# 时间复杂度（平均）	时间复杂度（最坏)	时间复杂度（最好)	空间复杂度	稳定性	复杂性
# O(n2)O(n2)	        O(n2)O(n2)	        O(n)O(n)	        O(1)O(1)	稳定	简单
# 冒泡排序对n个数据操作n-1轮，每轮找出一个最大（小）值。
# 操作只对相邻两个数比较与交换，每轮会将一个最值交换到数据列首（尾），像冒泡一样。
def bubble(bubbleList):
    listLength = len(bubbleList)
    for i in range(listLength-1):
        for j in range(listLength-i-1):
            if bubbleList[j] > bubbleList[j + 1]:
                bubbleList[j], bubbleList[j + 1] = bubbleList[j + 1], bubbleList[j]
    return bubbleList

"""改进一"""
# 设定一个变量为False，如果元素之间交换了位置，将变量重新赋值为True,最后再判断，在一次循环结束后，变量如果还是为False，则break退出循环，结束排序。
# def bubble_sort(items):
#     for i in range(len(items) - 1):
#         flag = False
#         for j in range(len(items) - 1 - i):
#             if items[j] > items[j + 1]:
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 flag = True
#         if not flag:
#             break
#     return items

"""改进二"""
# 上面这种写法还有一个问题，就是每次都是从左边到右边进行比较，这样效率不高，你要考虑当最大值和最小值分别在两端的情况。写成双向排序提高效率，即当一次从左向右的排序比较结束后，立马从右向左来一次排序比较。
# def bubble_sort(items):
#     for i in range(len(items) - 1):
#         flag = False
#         for j in range(len(items) - 1 - i):
#             if items[j] > items[j + 1]:
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 flag = True
#         if flag:
#             flag = False
#             for j in range(len(items) - 2 - i, 0, -1):
#                 if items[j - 1] > items[j]:
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     flag = True
#         if not flag:
#             break
#     return items


if __name__ == '__main__':
    bubbleList = [3, 4, 1, 2, 5, 8, 0]
    print(bubble(bubbleList))


