#!/usr/bin/env/ python
# -*- coding:utf-8 -*-
# Created by: Vanish
# Created on: 2019/3/28


class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        n = len(A)
        B = [0] * n
        B[0] = 1
        for i in range(1, n):
            B[i] = B[i-1] * A[i-1]
        tmp=1
        for i in range(0,n-1):
            j = n-2-i
            tmp *= A[j+1]
            B[j] *= tmp
        return B

if __name__ == '__main__':
    a = Solution()
    A = [1,2,3,4,5]
    print(a.multiply(A))