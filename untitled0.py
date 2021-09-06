#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 08:43:51 2021

@author: siddharthgehlot
"""

def factorial(n):
    if n==0:
        return 1
   
         
    return n*factorial(n-1)    
n=3       
print(factorial(n))        




def fact(n,res=1):
    if n==1:
        return res
    
    return fact(n-1,n*res)
    
    
print(fact(3,1))   


def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
n=6
print(fib(n-1)+fib(n-2))



def fibtail(n,a=0,b=1):
    if n==0:
        return a
    if n==1:
        return b
    return fibtail(n-1,a=b,b=a+b)
n=6
print(fibtail(n))
