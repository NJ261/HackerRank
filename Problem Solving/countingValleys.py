#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 01:47:28 2019

@author: nirav
"""

# Complete the countingValleys function below.
def countingValleys(n, s):
    state = True
    total = 0
    valleyCount = 0
    intial = ''
    for x in s:
        if state == True:
            state=False
            if x == 'D':
                total -= 1
                initial = 'down'
            else:
                total += 1
                initial = 'up'
        else:
            if x == 'D':
                total -= 1
            else:
                total += 1
            if total == 0:
                if initial == 'down':
                    valleyCount += 1
                state = True
    return valleyCount
            
if __name__ == '__main__':

    n = 12

    t = 'DDUUDDUDUUUD'
    
    result = countingValleys(n, t)
    print(result)
    
    
    
