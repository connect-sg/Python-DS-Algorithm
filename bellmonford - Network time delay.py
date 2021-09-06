#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:40:37 2021

@author: siddharthgehlot
"""

#bellmon-ford algorithm

time = [[1,4,2],[1,2,9],[4,2,-4],[2,5,-3],[4,5,6],[5,3,7],[3,2,3],[3,1,5]]
def bellmonford(time,N,k):
    distance = [float('Inf') for _ in range(N)]
    distance[k-1]=0
    
    
    for j in range(N-1):
       
      
        count=0
        for i in range(len(time)):
            source = time[i][0]
            target = time[i][1]
            weight = time[i][2]
            
            if distance[target-1]>distance[source-1]+weight:
                distance[target-1]=distance[source-1]+weight 
                count+=1
                print(source,target, distance)
        print(count)        
        if count==0:
          print('break')  
          break
     
    if max(distance)==float('Inf'):
        return -1
    else:
        return max(distance)
    
print(bellmonford(time,5,1))    
        