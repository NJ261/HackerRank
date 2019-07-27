#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 00:04:25 2019

@author: nirav
"""
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    result_alice, result_bob = 0, 0
    
    for i in range(0, len(a)):
        result = a[i] - b[i]
        if result > 0:
            result_alice += 1
        elif result < 0:
            result_bob += 1
    return [result_alice, result_bob]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
