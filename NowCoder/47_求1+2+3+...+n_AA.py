#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


# 32ms
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
# 加一个与算法判断 递归终止， 及 类的属性设置
class Solution:
    def Sum_Solution(self, n):
        # write code here
        def recur(n):
            n > 1 and recur(n - 1)
            self.res += n
            return self.res

        self.res = 0
        return recur(n)

    # def Sum_Solution(self, n):
    #     return n>0 and n+self.Sum_Solution(n-1)
    #  false等价0 print(3+False) out:3

if __name__ == '__main__':
    a = Solution()
    n = 5
    print(a.Sum_Solution(n))