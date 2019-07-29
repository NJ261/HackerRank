#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:26:08 2019

@author: nirav
"""
def timeConversion(s):
    remainingTime = s[2:-2]
    hour = s[:2]
    if s[-2:] == 'PM':
        hour = hourCheck(hour)
        return str(int(hour) + 12) + remainingTime
    else:
        hour = hourCheck(hour)
        return hour + remainingTime
    
def hourCheck(hour):
    if hour == '12':
        hour = '00'
    return hour

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
