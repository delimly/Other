# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:25:27 2023

@author: delic
"""

def linearSearch(list, target): 
    """
    

    Parameters
    ----------
    liat : list 
        DESCRIPTION.
    target :  string/ integer/ float
        DESCRIPTION.

    Returns
    -------
    The index position of the target if found, else returns None

    """
    
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return None 
    
    
list = [1,2,3,4,5]
target = 2



def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')
        

new_list = [x for x in range()]

new_list

index = linearSearch(list, target)
verify(index)
