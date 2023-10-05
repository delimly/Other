# Brute Force 

def countConstruct(target, wordBank):
    
    if target == '':
        return 1
    
    totalCount = 0
    
    for word in wordBank:
        if target.find(word) == 0:
            numways4Rest = countConstruct(target[len(word):], wordBank)
            totalCount += numways4Rest
            
            
    return totalCount
    
countConstruct('purple', ['purpl', 'p', 'ur', 'le', 'purp']) # 2
countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) # 1
countConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) # 
countConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o' , 't']) # 4
countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # 0  Takes long time to resolve 

# Memorisation 

def countConstruct2(target, wordBank, memo = None):
    
    if memo == None:
        memo = {} 
        
    if target in memo:
        return memo[target]
    
    if target == '':
        return 1
    
    totalCount = 0
    
    for word in wordBank:
        if target.find(word) == 0:
            numways4Rest = countConstruct2(target[len(word):], wordBank, memo)
            totalCount += numways4Rest
            
            
    memo[target] = totalCount
    return totalCount

countConstruct2('purple', ['purpl', 'p', 'ur', 'le', 'purp']) # 2
countConstruct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) # 1
countConstruct2('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) # 
countConstruct2('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o' , 't']) # 4
countConstruct2('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # 0  Takes long time to resolve 

# Tabulation - This is actually super efficent 

def countConstruct3(target, wordBank):
    
    table = [0 for i in range(len(target) + 1)]
    table[0] = 1 
    
    for i in range(len(target)): 
        for word in wordBank: 
            if word == target[i: (i + len(word))]:
                table[i+len(word)] += table[i]
    
    return table[len(target)]
    
    
    
countConstruct3('purple', ['purpl', 'p', 'ur', 'le', 'purp']) # 2
countConstruct3('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) # 1
countConstruct3('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) # 
countConstruct3('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o' , 't']) # 4
countConstruct3('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # 0
