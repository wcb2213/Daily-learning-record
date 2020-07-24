#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


# 23ms
# 输入n个整数，找出其中最小的K个数。
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        def big_heap(arr,root,end):
            while 1:
                child = root * 2 + 1
                if child>end:break
                if child+1<=end and arr[child]<arr[child+1]:
                    child+=1
                if arr[child]>arr[root]:
                    arr[child],arr[root]=arr[root],arr[child]
                    root=child
                else:
                    break

        if len(tinput)<k: return []
        # 建堆
        start= k//2-1
        for i in range(start,-1,-1):
            big_heap(tinput,i,k-1)
        # 删除操作：最后一个节点放到根节点处，新根节点递归下沉
        for i in range(k,len(tinput)):
            if tinput[i]<tinput[0]:
                tinput[i],tinput[0]=tinput[0],tinput[i]
                big_heap(tinput,0,k-1)
        # 排序：类似删除操作
        for i in range(k-1,0,-1):
            tinput[i],tinput[0]=tinput[0],tinput[i]
            big_heap(tinput,0,i-1)
        return tinput[:k]

if __name__ == '__main__':
    a = Solution()
    l = [4,5,1,6,2,7,3,8]
    print(a.GetLeastNumbers_Solution(l, 4))
