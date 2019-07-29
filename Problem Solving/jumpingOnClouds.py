#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 04:28:11 2019

@author: nirav
"""

def jumpingOnClouds(c):
    path = 0
    knownPath = 0
    length = len(c)
    for i in range(0, len(c)):
        if c[i] == 0:
            if i == knownPath:
                if i+2 < length - 1:
                    if c[i+2] == 0:
                        path += 1
                        knownPath = i+2
                    else:
                        path += 1
                        knownPath = i+1
                else:
                    path += 1
    return path
        
if __name__ == '__main__':

    c = [0 ,0 ,0 ,1 ,0 ,0]

    result = jumpingOnClouds(c)
    print(result)