#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 22:53:20 2019

@author: nirav
"""
name, score = [],[]

# recursion
def removeElements(minScore, dataA, dataB):
    if (minScore in dataA) == True:
        for i in range(0, len(dataA)):
            if str(dataA[i]) == str(minScore):
                dataA.pop(i)
                dataB.pop(i)
                removeElements(minScore, dataA, dataB)
                return dataA, dataB
    return dataA, dataB

if __name__ == '__main__':
    for _ in range(int(input())):
        name.append(input())
        score.append(input())
        
    minScore = min(score)
    score, name = removeElements(minScore, score, name)
    
    lowestNames = []
    minScore = min(score)
    for j in range(0, len(score)):
        if str(score[j]) == str(minScore):
            lowestNames.append(name[j])
            
    lowestNames.sort()
    print(lowestNames)