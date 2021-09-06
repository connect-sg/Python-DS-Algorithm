#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 07:00:58 2021

@author: siddharthgehlot
"""

#validate tree
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
    def validatetree(self,node,result):
      if node.left_node:
          self.validatetree(node.left_node,result)
      if result==[]:
          result.append(node.data)
         
      elif result.pop(0)<node.data:
          print('valid')
          result.append(node.data)
          
      else:
          return False
      print(result)
      if node.right_node:
          self.validatetree(node.right_node,result)
                   
      return True
 
        
             
if __name__ == '__main__':

    bst = BinarySearchTree()
    
    bst.insert(10)
    bst.insert(8)
    bst.insert(12)
    bst.insert(7)
    bst.insert(9)
    #bst.insert(11)
    #bst.insert(13)
    print(bst.validatetree(bst.root,[]) )
              