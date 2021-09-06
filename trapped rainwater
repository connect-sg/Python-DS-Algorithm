#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 08:27:54 2021

@author: siddharthgehlot
"""

array = [0,1,0,2,1,0,3,1,0,1,2]
def caltrapwater(array):
    a=0
    area = 0
    minarea=0
    for i in range(a,len(array)):
        
        if array[i]>0:
            for j in range(i+1,len(array)):
                
                #if array[j]==0:
                #    continue
                
                if array[j]>array[i]:
                      
                    for k in range(i+1,j):
                        minarea += array[k]
                        
                    area += min(array[i],array[j])*(j-i)-min(array[i],array[j])
                    print('area= {}  ,vali= {},valj= {},i ={},j= {},minarea= {}'.format(area,array[i],array[j],i,j,minarea))    
                    break
               
                    
        
            
                    
                
    return area 

print(caltrapwater(array))            
                
                