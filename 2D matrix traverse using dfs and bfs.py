#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:49:33 2021

@author: siddharthgehlot
"""

#2D matrix traversal 
matrix = [[5,4,1,7,6],
          [10,12,1,3,0],
          [45,67,8,2,18],
          [1,2,3,4,5],
          [9,8,7,6,5]
          ]

#depth first 

def traversedfs(matrix):
    direction =[[-1,0],[0,1],[1,0],[0,-1]]
    value = []
    seen =[[False for _ in range(len(matrix))] for _ in range(len(matrix))]
    print(seen)
    dfs(matrix,seen,value,0,0,direction)
    return value
    

def dfs(matrix,seen,value,row,col,direction):
         
          if row<0 or col<0 or  row>len(matrix)-1 or col>len(matrix[0])-1 or seen[row][col]==True:
              return 
          seen[row][col]=True 
          value.append(matrix[row][col])
          
          for i in direction:
             
              currpos = i
              dfs(matrix,seen,value,row+currpos[0],col+currpos[1],direction)
               
#print(traversedfs(matrix))  



#breadth first


def traversebfs(matrix):
    direction =[[-1,0],[0,1],[1,0],[0,-1]]
    value = []
    seen =[[False for _ in range(len(matrix))] for _ in range(len(matrix))]
   
    queue=[[0,0]]
    bfs(matrix,seen,value,queue,direction)
    return value   

def bfs(matrix,seen,value,queue,direction):
          
           
          while queue:
             print(queue) 
             actval = queue.pop(0)
             row = actval[0]
             col=actval[1]
             if row<0 or col<0 or  row>len(matrix)-1 or col>len(matrix[0])-1 or seen[row][col]==True:
              continue
            
             seen[row][col]=True
             value.append(matrix[row][col])
          
             
             for i in direction:
              
               currpos =i
               queue.append([row+currpos[0],col+currpos[1]])
               #print(queue)
print(traversebfs(matrix))               
               
          
         