#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 06:55:56 2019

@author: nirav
"""

# Complete the rotLeft function below.
def rotLeft(a, d):
    part_a = a[d:]
    for i in range(0, len(a[:d])):
        part_a.append(a[i])
    return part_a

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    
    