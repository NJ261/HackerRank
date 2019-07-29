#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 05:33:28 2019

@author: nirav
"""

def repeatedString(s, n):
    length = len(s)
    part_a = (n // length) * s.count('a')
    part_b = s[:(n % length)].count('a')
    return part_a + part_b

if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)