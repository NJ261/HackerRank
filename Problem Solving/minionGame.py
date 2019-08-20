#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 00:12:43 2019

@author: nirav
"""

def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)
    
    if (kevsc > stusc):
        print ("Kevin", kevsc)
    elif (kevsc < stusc):
        print ("Stuart", stusc)
    else:
        print ("Draw")
    

if __name__ == '__main__':
    s = 'BANANA'
    minion_game(s)