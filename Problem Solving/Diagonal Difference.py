#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 21:07:25 2019

@author: nirav

Description: Diagonal Difference
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
"""


def diagonalDifference(arr):
    n = int(len(arr) ** 0.5)
    oneSide = 0
    secondSide = 0
    
    count = 0
    for i in range(0, n):
        oneSide = oneSide + arr[i+count]
        count = count + n
        secondSide = secondSide + arr[count-(i+1)]
    
    result = oneSide - secondSide
    if result < 0:
        return result * -1
    
    return result
    

arr = [11, 2, 4, 4, 5,6, 10, 8, -12]
print(diagonalDifference(arr))

