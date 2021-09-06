#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 08:58:14 2021

@author: siddharthgehlot
"""

#reverse an array in place
array = [1,2,3,4,5]
def reversearray(array):
    i=0
    j= len(array)-1
    while i<=j:
        array[i],array[j]=array[j],array[i]
        i+=1
        j-=1
    return array    
print(reversearray(array))   
     
    