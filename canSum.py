
# CanSum : Brute Force

def canSum_bf(targetSum, numbers):
    
    if targetSum == 0 :
        return True 
    
    if targetSum < 0:
        return False 
    
    for num in numbers: 
        remainder = targetSum - num
        
        if canSum_bf(remainder, numbers) == True:
            return True 
        
    return False 


canSum_bf(7, [2,3]) # true
canSum_bf(7, [5,3,4,7]) # true
canSum_bf(7, [2,4]) # false
canSum_bf(8, [2,3,5]) # true
canSum_bf(300, [7., 14]) # false - Time effenciency takes long 

# CanSum : Memorisation

def canSum(targetSum, numbers, memo = None):
    
    if memo == None:
        memo = {}
    
    if (targetSum in memo):
        return memo[targetSum]
   
    if (targetSum == 0):
        return True 
    
    if (targetSum < 0):
        return False 
    
    for num in numbers: 
        remainder = targetSum - num
        
        if canSum(remainder, numbers, memo) == True: 
            memo[targetSum] = True
            return memo[targetSum]
    
    memo[targetSum] = False 
    return memo[targetSum]
    

canSum(7, [2,3]) # true
canSum(7, [5,3,4,7]) # true
canSum(7, [2,4]) # false
canSum(8, [2,3,5]) # true
canSum(300, [7, 14]) # false 


# CanSum : Tabulation 

def canSumTab(targetSum, numbers):
    
    table = [] 
    [table.append(False) for i in range(targetSum + 1)]
    table[0] = True
    
    for i in range(len(table)):
        if table[i]: 
            for num in numbers: 
                if (i+num) <= targetSum:
                    table[i+num] = True
                    
    return table[targetSum]
    
canSumTab(7, [2,3]) # true
canSumTab(7, [5,3,4,7]) # true
canSumTab(7, [2,4]) # false
canSumTab(8, [2,3,5]) # true
canSumTab(300, [7, 14]) # false
