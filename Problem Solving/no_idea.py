#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:42:48 2019

@author: nirav
"""

def findHappiness(n, a, b):
    
    a_plus_b = set().union(a,b)
    faltu = list(set(n) - set(a_plus_b))
    
    a_numbers = list(set(n) - set(faltu) - set(b))
    b_numbers = list(set(n) - set(faltu) - set(a))
    
    value_a = 0
    value_b = 0
        
    for i in a_numbers:
        value_a += n.count(i)
        
    for j in b_numbers:
        value_b += n.count(j)
    
    print(value_a - value_b)
    
    A = set(a)
    B = set(b)
    
    print(sum([(i in A) - (i in B) for i in n]))

n = [1,5,3]
a = [3,1]
b = [5,7]    
findHappiness(n,a,b)
















