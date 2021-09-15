#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:06:31 2021

@author: siddharthgehlot
"""

# count number of islands

array =[
        [1,1,1,1,0],
        [1,1,0,1,0],
        [1,1,0,0,1],
        [0,0,0,1,1]
        ]

array1=[
       [1,1,0,0,0],
       [0,0,1,1,0],
       [0,0,0,0,1],
       [1,1,1,1,1]
       ]

directions = [[0,1],[0,-1],[1,0],[-1,0]]
island =[[None for _ in range(len(array[0]))] for _ in range(len(array))]
queue=[[0,0]]

def numberIslands(array,directions):
    
    n=0
    for row in range(len(array)):
        for col in range(len(array[0])):
           
          queue = [[row,col]]
            
          if array[row][col]==1:
              
              n+=1
                
          
          
          while queue:
              
              val = queue.pop(0)
              row = val[0]
              col = val[1]
              if array[row][col]==1:
                  array[row][col]=0
                  for d in directions:
                      
                     nextrow = row+d[0]
                     nextcol = col+d[1] 
                      
                     if nextrow<0 or nextcol<0 or nextrow>=len(array) or nextcol>=len(array[0]):
                          
                          continue
                     
                      
                     if array[nextrow][nextcol]==1:  
                             
                             queue.append([nextrow,nextcol])
                             
                             
                       
                  
    return n

print(numberIslands(array1,directions))          
                   
              
                
                
           
           

            
        
        
        
        
            
        
            
            
        
        
        