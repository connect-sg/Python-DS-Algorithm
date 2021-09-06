#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:32:39 2021

@author: siddharthgehlot
"""

#8 employees - 0,1,2,3,4,5,6,7
#headID = 4
#manager -> [2,2,4,6,-1,4,4,5]
#information time -> [0,0,4,0,7,3,6,0]
class Node:
    def __init__(self,id,time):
        self.id = id
        self.adj_list=[]
        self.visited = False
        self.time = time
        
class graphBFS:
      
       def traverseTime(self,node):
           stack = []
           time = 0
           maxtime = 0
           
           stack.append(node)
           
           while stack:
               actval = stack.pop()
               
                
               #print('actval {}'.format(actval))
               #actval.visited = True
               
               
               for a in actval.adj_list:
                   stack.append(a)
                      
               time+=actval.time 
               if actval.adj_list==[]:
                   
                   time = node.time
               
               
               if time >maxtime:
                   maxtime=time
                   
                   
           return maxtime    
                   
       def Emp(self):
             headid= 4
             empId =[0,1,2,3,4,5,6,7]
             managerId = [2,2,4,6,-1,4,4,5]
             infoTime = [0,0,4,0,7,3,6,0]

             map ={} 
             adj_list ={}
             
             for i in range(len(empId)):
                 map[i]=[infoTime[0]]
                 adj_list[i]=[]
             for j in range(len(managerId)):
                 if managerId[j]!=-1:
                    adj_list[managerId[j]].append('node'+str(j))
             for i in range(len(empId)):
                 map[i].append(adj_list[i])
             #print(map) 
             return map
              
                 
if __name__=='__main__':
    g = graphBFS()
    g.Emp()
    
    """
    node0    = Node(0,g.Emp()[0][1],g.Emp()[0][2])
    node1    = Node(1,g.Emp()[1][1],g.Emp()[1][2])
    node2    = Node(2,g.Emp()[2][1],g.Emp()[2][2])
    node3    = Node(3,g.Emp()[3][1],g.Emp()[3][2])
    node4    = Node(4,g.Emp()[4][1],g.Emp()[4][2])
    node5    = Node(5,g.Emp()[5][1],g.Emp()[5][2])
    node6    = Node(6,g.Emp()[6][1],g.Emp()[6][2])
    node7    = Node(7,g.Emp()[7][1],g.Emp()[7][2]) 
    print(node4.adj_list)
    """
    node0 = Node(0,0)
    node1 = Node(1,0)
    node2 = Node(2,4)
    node3 = Node(3,0)
    node4 = Node(4,7)
    node5 = Node(5,3)
    node6 = Node(6,6)
    node7 = Node(7,0)
    
   
    node2.adj_list.append(node0)
    node2.adj_list.append(node1)
  
    node4.adj_list.append(node2)
    node4.adj_list.append(node5)
    node4.adj_list.append(node6)
    node5.adj_list.append(node7)
    node6.adj_list.append(node3)
   
    print(g.traverseTime(node4))
        
        
    
         
                       
            
               
        