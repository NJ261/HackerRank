#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 00:22:43 2019

@author: nirav
"""

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plusCount, minusCount, zero = 0, 0, 0
    arrayLength = len(arr)
    for i in range(0, len(arr)):
        if arr[i] > 0:
            plusCount += 1
        elif arr[i] < 0:
            minusCount += 1
    plusCount = plusCount / arrayLength
    minusCount = minusCount / arrayLength
    zero = 1 - plusCount - minusCount
    print(plusCount, '\n', minusCount, '\n', zero)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)