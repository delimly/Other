# Brute Force 

def canConstruct(target, wordBank):
    
    if target == '':
        return True
    
    for word in wordBank: 
        
        if target.find(word) == 0:
            suffix = target[len(word):]
            if (canConstruct(suffix, wordBank) == True):
                return True
            
    return False

canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) # True 
canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) # False
canConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o' , 't'])  # True
canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # False - Takes long time to resolve 

# Memorisation 

def canConstruct2(target, wordBank, memo = None):
    
    if memo == None:
        memo = {} 
        
    if target in memo: 
       return memo[target]
   
    if target == '':
        return True
    
    for word in wordBank: 
        
        if target.find(word) == 0:
            suffix = target[len(word):]
            if (canConstruct2(suffix, wordBank, memo) == True):
                memo[target] = True
                return True
            
    memo[target] = False
    return False

canConstruct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) # True 
canConstruct2('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) # False
canConstruct2('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o' , 't'])  # True
canConstruct2('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # False

# Tabulation 

def canConstruct3(target, wordBank):
    table = [False for i in range((len(target) + 1))]
    table[0] = True
    
    for i in range(len(target)):
        if table[i]:
            for word in wordBank:
                if (target[i:i+len(word)] == word):
                        table[i+len(word)] = True 
                    
    return table[len(target)]

canConstruct3('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) # True 
canConstruct3('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) # False
canConstruct3('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o' , 't'])  # True
canConstruct3('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # False

                    
                    