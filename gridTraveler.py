# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:13:10 2023

@author: delic
"""

def gridTraveler_simple(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    return gridTraveler(m - 1, n) + gridTraveler(m, n - 1)

gridTraveler_simple(1, 1) # 1
gridTraveler_simple(2, 3) # 3
gridTraveler_simple(3, 2) # 3
gridTraveler_simple(3, 3) # 6
gridTraveler_simple(18, 18) # 2333606220

def gridTraveler(m,n, memo = {}):
    
    key = (m , n)
    
    if key in memo :
        return memo[key]
    
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    memo[key] =  gridTraveler(m - 1, n, memo) + gridTraveler(m, n - 1, memo)
    
    return memo[key]


gridTraveler(1, 1) # 1
gridTraveler(2, 3) # 3
gridTraveler(3, 2) # 3
gridTraveler(3, 3) # 6
gridTraveler(18, 18) # 2333606220

def gridTravelerTab(m,n):
    table = [] 
    
    for i in range(m + 1):
        table.append([0 for i in range(n+1)])
        
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1): 
                
            current = table[i][j]
                
            if j+1 <= n:
                table[i][j+1] += current
                    
            if i + 1 <= m:
                table[i+1][j] += current 
    print(table)
    return table[m][n]
        

gridTravelerTab(1, 1) # 1
gridTravelerTab(2, 3) # 3
gridTravelerTab(3, 2) # 3
gridTravelerTab(3, 3) # 6
gridTravelerTab(18, 18) # 2333606220
