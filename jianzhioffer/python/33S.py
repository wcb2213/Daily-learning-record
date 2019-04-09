#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyList = [1]
        indexTwo, indexThree, indexFive = 0, 0, 0
        for i in range(index-1):
            newugly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
            uglyList.append(newugly)
            if newugly % 2 == 0:
                indexTwo += 1
            if newugly % 3 == 0:
                indexThree += 1
            if newugly % 5 == 0:
                indexFive += 1
        return uglyList[-1]

if __name__ == '__main__':
    a = Solution()
    print(a.GetUglyNumber_Solution(7))