#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/21


import functools
# 24ms
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return
        lmb = lambda x, y : int(str(x)+str(y)) - int(str(y)+str(x))
        res = sorted(numbers, key = functools.cmp_to_key(lmb))
        return int(''.join(map(str, res)))
        # return int(''.join([str(i) for i in res]))


if __name__ == '__main__':
    a = Solution()
    l = [3, 32, 321]
    print(a.PrintMinNumber(l))