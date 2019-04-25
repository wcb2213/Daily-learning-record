#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/4/24


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array)<1:
            return []
        res = [array[0]] # 累计和
        pre = array[0]
        for i in range(1,len(array)):
            if pre >= 0:
                pre = pre+array[i]
                res.append(pre)
            else:
                pre = array[i]
                res.append(pre)
        a2 = res.index(max(res))
        if min(res[0:a2])>0:
            a1 = -1
        else:
            for i in range(a2):
                if res[a2-1-i] < 0:
                    a1 = a2-1-i
                    break
        return array[a1+1:a2+1],max(res) # [6, 3, 1, 8, -7, 1, 3, 5]

if __name__ == '__main__':
    a = Solution()
    l = [6,-3,-2,7,-15,1,2,2]
    print(a.FindGreatestSumOfSubArray(l))