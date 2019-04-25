#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/22


# 27ms
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 每得到一个丑数，必然得到三个新的丑数（*2，*3，*5） 初始为[1]，然后做一个类似生成器的东西
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyList = [1]
        indexTwo, indexThree, indexFive = 0, 0, 0
        for i in range(index-1):
            newugly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5) # 排序简单
            uglyList.append(newugly)
            # 判断乘到哪儿了 2*3 3*2 2，3都得+1 所以三个 if
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