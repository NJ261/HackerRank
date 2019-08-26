#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 02:05:07 2019

@author: nirav
"""

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        subStr = string[i:i+k]
        if len(set(subStr)) != k:
            uniqueChars = list(set(subStr))
            processedStr = list(subStr)
            processedStr.reverse()
            for i in uniqueChars:
                count = processedStr.count(i)
                if count > 1:
                    for j in range(0, count-1):
                        processedStr.pop(processedStr.index(i))
            processedStr.reverse()      
            print(''.join(processedStr))
            
        else:
            print(subStr)
            

        
    

if __name__ == '__main__':
    string, k = 'AABCAAADA',3
    merge_the_tools(string, k)