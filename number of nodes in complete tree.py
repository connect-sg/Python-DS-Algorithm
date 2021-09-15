#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:27:34 2021

@author: siddharthgehlot
"""

#NUMBER OF NODES IN COMPLETE TREE
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
    def completeTreeNodes(self):
        
            if self.root is None:
                return None
            else:
                maxdepth,nodeNo = self.nodeAtSecondLastLevel(self.root.leftChild,0,1,0)
                num = self.numberAtLastLevel(self.root.leftChild,1,nodeNo,maxdepth)
               
                return num
    def numberAtLastLevel(self,node,level,nodeNo,maxdepth):
         if node is None:
             return nodeNo
         while node.leftChild and level<maxdepth-1:
             
             level+=1
             #print(level)
             node = node.leftChild
         
             
         if node.leftChild and level==maxdepth-1:
             nodeNo+=1
             
         if node.rightChild and level==maxdepth-1:
             nodeNo+=1
             
             return self.numberAtLastLevel(node.rightChild,level,nodeNo,maxdepth)
             
         return nodeNo    
             
             
    def nodeAtSecondLastLevel(self,node,level,nodeNo,maxdepth) :
        if node is None:
            
            return maxdepth+1,nodeNo
        if node.leftChild:
            level+=1
            nodeNo+=2**level
            maxdepth+=1
        return self.nodeAtSecondLastLevel(node.leftChild,level,nodeNo,maxdepth)
        
        
            
        return nodeNo    
if __name__=='__main__':
       bst = BinarySearchTree()
       bst.insert(8)
       bst.insert(6)
       bst.insert(7)
       bst.insert(10)
       bst.insert(4)
       bst.insert(5)
       bst.insert(3)
       bst.insert(9)
       bst.insert(11)
       print(bst.completeTreeNodes())            
        
        
            