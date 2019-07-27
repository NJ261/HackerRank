#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:15:23 2019

@author: nirav
"""

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minNum = arr.pop(arr.index(max(arr)))
    maxNum = arr.pop(arr.index(min(arr)))
    remainSum = sum(arr)
    print(remainSum+minNum, remainSum+maxNum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)