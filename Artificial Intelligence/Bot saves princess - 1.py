#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:12:52 2019

@author: nirav
"""

def displayPathtoPrincess(n, grid):
    # find princess and mario
    for idx, row in enumerate(grid):
        if 'p' in row:
            princess = (idx, row.index('p'))
        if 'm' in row:
            mario = (idx, row.index('m'))
    
    # negative row difference implies UP
    # negative col difference implies LEFT
    drows = princess[0] - mario[0]
    dcols = princess[1] - mario[1]
    
    upDown(drows, dcols)
    return drows, dcols
    
def upDown(drows, dcols):
    
    if drows < 0:
        for i in range(0, (drows * -1)):
            print("UP")
        leftRight(dcols)
        
    elif drows > 0:
        for i in range(0, drows):
            print("DOWN")
        leftRight(dcols)
        
    else:
        leftRight(dcols)
    
def leftRight(dcols):
    
    if dcols < 0:
        for i in range(0, (dcols * -1)):
            print("LEFT")
        
    if dcols > 0:
        for i in range(0, dcols):
            print("RIGHT")
    
w = 4
grid = ['----', 'p---', '----','---m']

r,c = displayPathtoPrincess(w,grid)














