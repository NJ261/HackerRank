#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 00:35:50 2019

@author: nirav
"""

# Complete the staircase function below.
def staircase(n):
    imageSymbol = '#'
    space = ' '
    for i in range(0, n):
        a = (space * (n - (i+1)) ) + (imageSymbol * (i+1))
        print((space * (n - i) ) + (imageSymbol * (i+1)))
        print(len(a))

if __name__ == '__main__':
#    n = int(input())
    n = 4

    staircase(n)
