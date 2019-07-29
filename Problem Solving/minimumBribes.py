#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 07:57:31 2019

@author: nirav
"""

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes=0
    for i in range(len(q)-1,-1,-1):

        if(q[i]-1 - i > 2):
            print("Too chaotic")
            return
        for j in range(max(0,q[i]-2),i):
            if(q[j]>q[i]):
                bribes = bribes + 1
    print(bribes)

if __name__ == '__main__':

        q = [1,2 ,5 ,3 ,7 ,8 ,6 ,4]

        minimumBribes(q)