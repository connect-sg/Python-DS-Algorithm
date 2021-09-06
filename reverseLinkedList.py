#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 17:55:19 2021

@author: siddharthgehlot
"""

#reverse a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
     def __init__(self):
         self.head =None
     def insert(self,data):
           insertData = Node(data)
           if self.head is None:
               self.head = insertData 
           else:
               insertData.next = self.head
               self.head = insertData
     def traverse(self):
            printval = self.head
            while printval is not None:
                print(printval.data)
                printval = printval.next
     def reverse(self,node):
         value = node
         prev = None
         while value is not None:
             nextnode = value.next
             value.next = prev
             prev = value
             value=nextnode
         if value is None:
            self.head =prev
           
     def reversell(self,node,prev):
          if node is None:
             self.head=prev
             return self.head
              
          value = node
          nextnode = value.next
          node.next =prev
          prev = value 
          value = nextnode
          
          
          self.reversell(value,prev)
          
          
          
          
              
              
if __name__=='__main__':
     ll = linkedlist()
     ll.insert(1)
     ll.insert(2)
     ll.insert(9)
     ll.traverse() 
     ll.reverse(ll.head)
     ll.traverse()
     ll.reversell(ll.head,None)
     ll.traverse()             