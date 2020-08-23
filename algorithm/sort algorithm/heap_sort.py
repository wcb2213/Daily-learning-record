#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/5/5


# 1、插入：没做，类似 3建堆，上浮
"""堆排序"""
# 3、堆调整：最大堆的所有子树都是最大堆，因此可以自顶向下做下沉
def big_endian(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1  # 左节点下标 如果下标从1开始，则为 root*2
        if child > end:  # 没有孩子节点时，无需调整，跳出循环
            break
        # 判断有无右节点，并选择值更大的下标 右节点下标=左节点下标+1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        # 父节点小于子节点直接换位置 调整过的子节点可能需要继续调整，故循环下去
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:  # 父子节点顺序正常 无需调整
            break

# 2、删除操作：最后一个节点放到根节点处，新根节点递归下沉
# 4、排序：使用操作（2），依次取出最大值
def heap_sort(arr):
    # 无序区大根堆排序
    # root=（child-1）//2=(len(arr)-1-1)//2=len(arr)//2-1
    first = len(arr) // 2 - 1

    # 构成最大堆：利用3堆调整从下到上，从右到左对每个非叶子节点进行调整
    for start in range(first, -1, -1):
        big_endian(arr, start, len(arr) - 1)

    # 4排序 # 删除根节点，每次删除相当于提取最大值
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        big_endian(arr, 0, end - 1)  # 从顶开始重新调整成最大堆
    return arr

if __name__ == "__main__":
    l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
    print(heap_sort(l))