#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:57:10 2021

@author: siddharthgehlot
"""

#RIGHT SIDE VIEW OF A TREE
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent
        self.visited = False
class BinarySearchTree:
    def __init__(self):
         self.root = None
         
    def insert(self,data):
        insertNode = Node(data,None)
        if self.root is None:
            self.root = insertNode 
        else:
            self.insertData(self.root,data)
            
    def insertData(self,node,data):
         if data>node.data:
             if node.rightChild:
                 self.insertData(node.rightChild,data)
             else:
                 node.rightChild = Node(data,node)
         else:
             if node.leftChild:
                 self.insertData(node.leftChild,data)
             else:
                 node.leftChild = Node(data,node)

    def rightSideView(self):
        if self.root is None:
            return None 
        else:
            return self.rightSide(self.root,0,[])
            
    def rightSide(self,node,n,array):
         if node is None:
             return 
         
        
         if n>=len(array):
             array.append(node.data)
         
             
         if node.rightChild:
             self.rightSide(node.rightChild,n+1,array)
         if node.leftChild:
             self.rightSide(node.leftChild,n+1,array)
         
         
         return array
               
  
if __name__=='__main__':
       bst = BinarySearchTree()
       bst.insert(5)
       bst.insert(3)
       bst.insert(2)
       bst.insert(8)
       bst.insert(10)
       #bst.insert(13)
       bst.insert(1)
       print(bst.rightSideView())         
             
