#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 08:38:12 2021

@author: siddharthgehlot
"""

# WALL AND GATES
#distance to reach from one gate to another

    
er = float('inf')
gate = 0
wall = -1
visited = 2
gatevisited =3
    
def solveWallGate():
    array = [
            [er,wall,gate,er],
            [er,er,er,wall],
            [er,wall,er,wall],
            [gate,wall,er,er]
             ]
    
    direction = [[0,1],[0,-1],[-1,0],[1,0]]
    row=0
    col=0
    while array[row][col]!=gate:
        
        col+=1
    print(row,col)    
    
    return wallGate(array,direction,row,col,0)

def wallGate(array,direction,row,col,n):
            if array[row][col]==gate and row!=0 and col!=0:
                return n
        

            if array[row][col]==gate or array[row][col]==er or array[row][col]==gatevisited:
                
                if array[row][col]==gate:
                     array[row][col]=gatevisited
                if array[row][col]==er:
                    array[row][col]=visited
             
                for d in direction:
                    nextrow = row+d[0]
                    nextcol = col+d[1]
                    
                    if nextrow<0 or nextcol<0 or nextrow>=len(array) or nextcol>=len(array[0]) or array[nextrow][nextcol]==wall or array[nextrow][nextcol]==visited:
                        continue
                    print(nextrow,nextcol)
                    
                        
                    if array[nextrow][nextcol]==gatevisited:
                        n=0
                     
                    return wallGate(array,direction,nextrow,nextcol,n+1)
                
            return n   
                
print(solveWallGate())                
                    
                    
                    
                    