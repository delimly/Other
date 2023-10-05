# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:18:30 2023

@author: delic
"""

# Dynamic Programming : Fibbonacci Sequence

def fib_simple(n): 
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


fib_simple(1)
fib_simple(9)
fib_simple(50)

# Fibbonacci Sequence: IMPROVED 

def fib(n, memo = {}): 
    
    if (n in memo):
        return memo[n]
    
    if n <= 2:
        return 1
    
    memo[n]  = fib(n-1, memo) + fib(n-2, memo)
    
    return memo[n]

fib(50)

def fibTab(n): 
    
   fibs = [0,1]
    
   for i in range(2 ,n + 1):
        fibs.append(fibs[-1] + fibs[-2])
        
   return fibs[n]

fibTab(6) # 8 
fibTab(7) # 13
fibTab(8) # 21
fibTab(50) # 12586269025
