#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 13:16:11 2021

@author: siddharthgehlot
"""

# VALIDATE BINARY TREE

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
                 
    def insertRandom(self,data):
             
             if self.root is None:
                 self.root = Node(data,None)
             else:
                self.insertRandomData(self.root,data)
    def insertRandomData(self,node,data):
             if node.leftChild:
                 self.insertRandomData(node.rightChild,data)
             else:
                 node.leftChild = Node(data,node)
             if node.rightChild:
                 self.insertRandomData(node.leftChild,data)
             else:
                 node.rightChild = Node(data,node)
                 
                 
                 
                 
                 
                 
    def binaryTree(self):
        if self.root is None:
            return None 
        
        else:
            left = -float('inf')
            right = float('inf')
            return self.validateTree(self.root,left,right)
        
            
            
    def validateTree(self,node,left,right):
             if node is None:
                 return  
         
             if node.data>left:
                 if node.leftChild:
                   return self.validateTree(node.leftChild,left,node.data)
             else:
                 return False
             
             if node.data<right:
                 if node.rightChild:
                    return self.validateTree(node.rightChild,node.data,right) 
             else:
                  return False
              
             return True 
     
if __name__=='__main__':
       bst = BinarySearchTree()
       """
       bst.insert(8)
       bst.insert(6)
       bst.insert(7)
       bst.insert(10)
       bst.insert(4)
       bst.insert(5)
       bst.insert(3)
       bst.insert(9)
       bst.insert(11)
       """
       bst.insertRandom(4)
       bst.insertRandom(3)
       bst.insertRandom(5)
       bst.insertRandom(10)
       print(bst.binaryTree())          
       