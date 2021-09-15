#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:24:41 2021

@author: siddharthgehlot
"""

#ROTTEN ORANGES
def oranges():
    array = [
             [2,1,1,0,0],
             [1,1,1,0,0],
             [0,1,1,1,1],
             [0,1,0,0,1]
            ]
    array1=[
            [2,1,1,0,0],
            [1,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
             ]
    directions =[[0,1],[0,-1],[1,0],[-1,0]]
    queue =[[0,0]]
    t=0
    return rottenOranges(array1,queue,t,directions)
    
def rottenOranges(array,queue,t,directions):
    #using bfs
    l = len(queue)
    
    #print(queue,l)
    if l==0:
        return t-1
    
    
    
    while l>0:   
         val = queue.pop(0)
         row = val[0]
         col = val[1]
         
         
         
         if array[row][col]==2:
             
             for d in directions:
                 nextrow = row + d[0]
                 nextcol = col + d[1]
                 if nextrow<0 or nextcol<0 or nextrow>=len(array) or nextcol>=len(array[0]):
                     continue
                 if array[nextrow][nextcol]==1:
                  
                   queue.append([nextrow,nextcol])
                
                   array[nextrow][nextcol]=2
                 
                 
         l-=1                     
         
    print(array,queue,t)     
    return rottenOranges(array,queue,t+1,directions)
    

print(oranges())
         