#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 06:02:32 2019

@author: nirav
"""

# Complete the hourglassSum function below.
def hourglassSum(arr):
    temp = []
    mainMatrix = []
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[i]) - 2):
            for m in range(3):
                for n in range(3):
                    temp.append(arr[i+m][j+n])
            temp.pop(3)
            temp.pop(4)
            mainMatrix.append(sum(temp))
            temp = []
    return max(mainMatrix)
                    
                

if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], 
           [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], 
           [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)
    print(max(result))