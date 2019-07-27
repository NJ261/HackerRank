#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 23:26:04 2019

@author: nirav

Description: Extra Long Factorials
"""

#!/bin/python3

import sys

# Complete the diagonalDifference function below.
def findHappiness(n, a, b):
    
    tempN = n[:]
    tempNN = n[:]
    
    listA = list(set(n) - set(a))
    listB = list(set(n) - set(b))
    
    for i in range(0, len(listA)):
        for j in range(0, len(n)):
            if (listA[i] == n[j]) == True:
                tempN.remove(listA[i])
    
    for i in range(0, len(listB)):
        for j in range(0, len(n)):
            if (listB[i] == n[j]) == True:
                tempNN.remove(listB[i])
            
    print(len(tempN) - len(tempNN))

if __name__ == '__main__':

    n = [1,5,3,3,3,8,8]
    a = [3,1]
    b = [5,7]
    
    findHappiness(n, a, b)
    

