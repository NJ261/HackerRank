#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:42:48 2019

@author: nirav
"""

def findHappiness(n, a, b):
    
    A = set(a)
    B = set(b)
    
    print(sum([(i in A) - (i in B) for i in n]))

n = [1,5,3]
a = [3,1]
b = [5,7]    
findHappiness(n,a,b)
















