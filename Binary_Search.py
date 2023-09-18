# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 17:53:25 2023

@author: delic
"""

def binarySearch(list, target):
    first = 0 
    last = len(list) - 1
    
    
    while first <= last:
        midpoint = (first + last) // 2 
        
        if list[midpoint] == target: 
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else: 
            last = midpoint - 1
            
    return None


def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')
        


list1 = [x for x in range(12)]

list1
target = 9

index = binarySearch(list1, target)

verify(index)