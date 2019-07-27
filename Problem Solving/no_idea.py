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
    
import time
start = time.time()    
inputFn = "input06.txt"

with open(inputFn) as inputFileHandle:
    file = inputFileHandle.read()
    
x = [s.strip() for s in file.splitlines()]
n = x[1].split()
a = x[2].split()
b = x[3].split()
findHappiness(n,a,b)
end = time.time()

print(end-start)
'''
n = 100000
a = 14544
b = 14544

a + b = 29088
faltu = 85268

set(n) = 90641




'''















