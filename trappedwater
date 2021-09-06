#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:41:38 2021

@author: siddharthgehlot
"""

array = [0,1,0,2,1,0,3,1,0,1,2]

def trapwater(array):
        
        watertrapped=0
        maxleft = 0
       
        for i in range(len(array)):
            if array[i]>maxleft:
                maxleft = array[i]
            for mr in range(i,len(array)):
                maxright = array[mr]
                if array[mr]>maxright:
                    maxright = array[mr]
                    
            z=min(maxright,maxleft)-array[i]        
            if z<0:
                z=0
           # print(maxright,maxleft,array[i],z)    
            watertrapped+=z
                
            
        return watertrapped 
print(trapwater(array))              
                    
                    
    
                