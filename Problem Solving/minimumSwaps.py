#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 01:02:06 2019

@author: nirav
"""

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    for i in range(0,len(arr)-1):
        if arr[i] != i+1:
            #temp = arr.index(i+1)
            arr[arr.index(i+1)], arr[i] = arr[i], arr[arr.index(i+1)]
            count += 1
             
    return count


arr = [1 ,3 ,5 ,2 ,4 ,6 ,7]

res = minimumSwaps(arr)

print(res)