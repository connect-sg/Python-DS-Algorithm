#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:37:41 2021

@author: siddharthgehlot
"""

#bianry tree level order 
class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):

        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)
            
            
    def levelorder(self,level):
         if self.root is None:
            return None 
         else:
            res = [] 
            val =self.levelOrderAlgo(self.root,level)
            for i in val:
                res.append(i.data)
            return res

    def levelOrderAlgo(self,node,level):
       
        queue=[]
        queue.append(node)
        l=0
        while queue and l<=level:
             length = len(queue)
             result=[]
             while length >0:    
              actval = queue.pop(0)
              result.append(actval)
            
              if actval.left_node:
                queue.append(actval.left_node)
                
              if actval.right_node:
                queue.append(actval.right_node)
              length-=1  
             l+=1
            
        
        return result  
            
            


        
            
if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    print(bst.levelorder(4))
    
            