#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 07:04:22 2019

@author: nirav
"""

def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)