#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 03:10:36 2019

@author: nirav
"""

if __name__ == '__main__':
    n = int(input())
    words, count = [], []
    
    for i in range(0, n):
        word = str(input())
        if words.count(word) == 0:
            words.append(word)
            count.append(str(1))
        else:
            wordIndex = words.index(word)
            count[wordIndex] = str(int(count[wordIndex]) + 1)
            
    print(len(words))
    print(' '.join(count))
    
    '''
    # fast sol:
    from collections import Counter, OrderedDict
    class OrderedCounter(Counter, OrderedDict):
        pass
    d = OrderedCounter(input() for _ in range(int(input())))
    print(len(d))
    print(*d.values())
    '''
    
        
    
    
    