#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:51:56 2021

@author: siddharthgehlot
"""

#kth largest element of the array
array=[5,4,1,2,6,3]
def quickselect(a,k):
    pivot = algo(array,k,0,len(array))
    
    while pivot!=k:
      #print(pivot)  
      if pivot<k:
        pivot=algo(array,k,pivot+1,len(array))
      elif pivot >k:
          pivot=algo(array,k,0,pivot-1)

    return array[pivot],pivot
          
    
def algo(array,k,l,r):
     pivot=(l+r)//2
    
     low = l
     high = r-1
     
     i=low
     j=low
     #swap pivot and high value 
     array[pivot],array[high]=array[high],array[pivot]
     
     while j<high:
      
      if array[j]<=array[high]:
         #swap i and j and increment i by 1
         array[j],array[i]=array[i],array[j]
         i+=1
         
      j+=1   
     array[high],array[i]=array[i],array[high]
     pivot = i
     
     
     return pivot
 
    
print(quickselect(array,0)) 
print(quickselect(array,1)) 
print(quickselect(array,2))
print(quickselect(array,3))
print(quickselect(array,4))
print(quickselect(array,5))
      
         
             
         
     
        
    