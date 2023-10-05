# Memorisation 

def howSum(targetSum, numbers , memo = None): 
    
    if memo == None:
        memo = {}
        
    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0 :
        return []
    
    if targetSum < 0:
        return None 
    
    for num in numbers:
        remainder = targetSum - num 
        
        remainderResult = howSum(remainder, numbers)
        
        if remainderResult is not None:
            remainderResult.append(num)
            memo[targetSum] = remainderResult            
            return memo[targetSum]
    
    memo[targetSum] = None
    
    return memo[targetSum]


howSum(7, [2,3]) # [3,2,2]
howSum(7, [5,3,4,7]) # [4,3]
howSum(7, [2,4]) # null
howSum(8, [2,3,5]) #  [2,2,2,2]
howSum(300, [7, 14])  # null 

# Tabulation 

def howSumTab(targetSum, numbers):
    
        table = []
        [table.append(None) for i in range(targetSum + 1)]
        table[0] = [] 
        
        for i in range(len(table)): 
            if table[i] is not None:
                for k in numbers:
                    if (i + k) <= targetSum:
                        table[i + k] = table[i].copy()
                        table[i + k].append(k)
        
        return table[targetSum]
    
howSumTab(7, [2,3]) # [3,2,2]
howSumTab(7, [5,3,4,7]) # [4,3]
howSumTab(7, [2,4]) # null
howSumTab(8, [2,3,5]) #  [2,2,2,2]
howSumTab(300, [7, 14])  # null 
