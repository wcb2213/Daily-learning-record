#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/6/14


"""归并排序"""
# 时间复杂度（平均）	时间复杂度（最坏)	时间复杂度（最好)	空间复杂度	稳定性	复杂性
# O(nlog2n)O(nlog2n)	O(nlog2n)O(nlog2n)	O(nlog2n)O(nlog2n)	O(n)O(n)	稳定	较复杂
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right): # 两个有序链表合成一个有序链表
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result

if __name__ == '__main__':
    lists = [2, 3, 5, 7, 1, 4, 6, 15, 5, 2, 7, 9, 10, 15, 9, 17, 12]
    print(MergeSort(lists))