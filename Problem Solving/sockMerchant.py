#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 01:28:20 2019

@author: nirav
"""

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    uniqueElements = set(ar)
    pairCount = []
    for elem in uniqueElements:
        count = ar.count(elem)
        if count >= 2:
            pairCount.append(count//2)
    return sum(pairCount)
            

if __name__ == '__main__':

    n = 9

    ar = [10,20,20,10,10,30,50,10,20]
    print(sockMerchant(n, ar))
