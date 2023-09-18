

def mergeSort(list):
    
    """
    Sorts a list in ascending order 
    
    Returns a new sorted list
    
    1. Divide: Find the midpoint of the list and divide into sublists
    2. Conquer: Recursively sort the sublits created in previous step
    2. Combine: Merge tje sorted sublists created in previous step
    
    The alorithm runs in O((nlog(n)))  - note for python this is mutiplied by k
    """
    
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = mergeSort(left_half)
    right = mergeSort(right_half)
    
    return merge(left, right)


def split(list):
    
    """
     Divides the unsorted list at mid point into sublists 
     Returns two sublists - left and right 
     
     This take O(log(n)) time - note for python this is mutiplied by k
    """
    
    midpoint = len(list) // 2
    
    left = list[:midpoint]
    right = list[midpoint:]
    
    return left, right 
    
def merge(left, right):
    
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list 
    
    This takes O(n) 
    """
    
    l = [] 
    i = 0 
    j = 0 
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1

        else: 
            l.append(right[j])
            j += 1
            
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1
        
    return l
        
        
# Example

alist = [11,2,39,27,92,32,1,16,54,28,13]

l2 = mergeSort(alist)

print(l2)

left1, right1 = split(alist)

type(a)

def verifySorted(list):
    n = len(list)
    
    if n == 0 or n == 1: 
        return True
    
    return list[0] < list[1] and verifySorted(list[1:])

print(verifySorted(alist)) # This is false

print(verifySorted(l2)) # This is true 

# The merge sort algoithm has a O(nlog(n)) 
