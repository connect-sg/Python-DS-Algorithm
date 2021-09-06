#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 08:29:51 2021

@author: siddharthgehlot
"""

#binary search

array =[1,3,3,5,5,5,6,6]
def binarysearch(array,target):
    mid = 0
    print(mid)
    
    l=mid
    r = mid
    
    while target>array[l]:
        l+=1
        print(l)
    while (l+r)<len(array) and target==array[l+r]: 
            r+=1
            
            
    return [l,l+r-1]    
print(binarysearch(array,5))
        
            
        