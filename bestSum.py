
# BestSum - Dynamic Programing 

"""
The Brute Force Approach
"""

def bestSum(targetSum, numbers):
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            combination = remainderCombination[:] + [num]
            if  (shortestCombination == None) or (len(combination) < len(shortestCombination)): 
                shortestCombination = combination
                
    return shortestCombination

# Test Cases 

bestSum(7, [5,3,4,7]) # [7]
bestSum(8, [2,3,5]) # [3,5]
bestSum(8, [1,4,5]) # [4,4]
bestSum(100, [1,2,5,25]) # [25,25,25,25]

"""
The Memorisation Approach
"""

def bestSum2(targetSum, numbers, memo = None):
    
    if memo == None:
        memo = {} 
        
    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination = None
    
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum2(remainder, numbers, memo = memo)
        if remainderCombination is not None:
            combination = remainderCombination[:] + [num]
            if  (shortestCombination is None) or (len(combination) < len(shortestCombination)): 
                shortestCombination = combination
                
    memo[targetSum] = shortestCombination
    return shortestCombination

# Test Cases 

bestSum2(7, [5,3,4,7]) # [7]
bestSum2(8, [2,3,5]) # [3,5]
bestSum2(8, [1,4,5]) # [4,4]
bestSum2(100, [1,2,5,25]) # [25,25,25,25]

"""
The Tabulation Approach
"""

def bestSum3(targetSum, numbers):
    table = [None for i in range(targetSum + 1)]
    table[0] = [] 
    for i in range(targetSum):
        if table[i] is not None: 
            for num in numbers: 
                if (i + num) <= targetSum:
                    candidate = table[i].copy()
                    candidate.append(num)
                    if table[i+num] is None or (len(table[i+num])) > len(candidate): 
                        table[i+num] = candidate
    return table[targetSum]

# Test Cases 

bestSum3(7, [5,3,4,7]) # [7]
bestSum3(8, [2,3,5]) # [3,5]
bestSum3(8, [1,4,5]) # [4,4]
bestSum3(100, [1,2,5,25]) # [25,25,25,25]
