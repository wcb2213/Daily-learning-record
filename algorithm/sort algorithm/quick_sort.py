#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


"""快速排序"""
# 时间复杂度（平均）	时间复杂度（最坏)	时间复杂度（最好)	空间复杂度	        稳定性	复杂性
# O(nlog2n)O(nlog2n)	O(n2)O(n2)	        O(nlog2n)O(nlog2n)	O(nlog2n)O(nlog2n)	不稳定	较复杂
def quick_sort(lists):
    if len(lists) < 2:
        return lists
    pivot = lists.pop()  # 选取基准值，也可以选取第一个或最后一个元素,必须从原始数组中移除基准值，否则会死循环
    left, right = [], []
    for i in range(len(lists)):
        if lists[i] <= pivot:
            left.append(lists[i])
        else:
            right.append(lists[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
    lists = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    print(quick_sort(lists))