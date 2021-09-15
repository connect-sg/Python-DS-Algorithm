#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:15:22 2021

@author: siddharthgehlot
"""

#REMOVE THE LEAST AMOUNT OF BRACKETS SO THAT THE STRING IS VALID

string = 'a((bv(d))'
def validateString(string):
   array = list(string) 
   a=[]
   pt1 = len(array)-1
   st=''
   map={'(':')'}
   while pt1>0: 
    
    if array[pt1] ==')':
        a.append(array[pt1])
        
    else:
        
        if array[pt1] =='(':
            print(array[pt1])
            if len(a)>0:
                if map[array[pt1]]!=a[-1]:
                    array.pop(pt1)
                if map[array[pt1]]==a[-1]:
                    a.pop()
            else:
                array.pop(pt1)
      
                 
    pt1-=1  
   for i in array:
         st+=i       
   return st        
print(validateString(string))