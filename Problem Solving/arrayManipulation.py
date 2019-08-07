#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 03:50:57 2019

@author: nirav
"""

def arrayManipulation(n, queries):
    array = [0] * n
#    for i in range(0, len(queries)):
#        for j in range(queries[i][0], queries[i][1]+1):
#            array[j-1] = array[j-1] + queries[i][2] 
#        print(array)
        
    print('****')
    for i in range(0, len(queries)):
        b = array[:]
        b[queries[i][0]-1::] = [queries[i][2]] * (queries[i][1] - queries[i][0] + 1) + b[queries[i][1]+1:]
        print(b, '*********')
        array = [x+y for x,y in zip(array,b)]
        print(array)
    return max(array)

n = 10

queries = [[2,6,8], [3,5,7], [1,8,1], [5,9,15]]

result = arrayManipulation(n, queries)

print(result)
