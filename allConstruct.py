
def allConstruct(target, wordBank):
    
    if target == '':
        return [[]]
    
    resultList = [] 
    
    for word in wordBank: 
        if target.find(word) == 0: 
            suffix = target[len(word):]
            current2dList = allConstruct(suffix, wordBank)
            for current1d in current2dList:
                current1d = [word] + current1d
                resultList.append(current1d)
                
    return resultList 
                
    
allConstruct('purple', ['purpl', 'p', 'ur', 'le', 'purp']) 
# [ 
#   ['purp', 'le'],
#   ['p', 'ur',  'p' , 'le']
# ]
allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']) 
# [ 
#   ['ab', 'cd', 'ef'],
#   ['ab', 'c', 'def'],
#   ['abc', 'def'],
#   ['abcd', 'ef']
# ]
allConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']) 
# [] 
allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) 
# []  Takes long time to resolve 


def allConstruct2(target, wordBank, memo = None):
    
    if memo == None:
        memo = {} 
        
    if target in memo:
        return memo[target]
    
    if target == '':
        return [[]]
    
    resultList = [] 
    
    for word in wordBank: 
        if target.find(word) == 0: 
            suffix = target[len(word):]
            current2dList = allConstruct2(suffix, wordBank, memo)
            for current1d in current2dList:
                current1d = [word] + current1d
                resultList.append(current1d)
           
    memo[target] = resultList
    return resultList 

    
allConstruct2('purple', ['purpl', 'p', 'ur', 'le', 'purp']) 
# [ 
#   ['purp', 'le'],
#   ['p', 'ur',  'p' , 'le']
# ]
allConstruct2('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']) 
# [ 
#   ['ab', 'cd', 'ef'],
#   ['ab', 'c', 'def'],
#   ['abc', 'def'],
#   ['abcd', 'ef']
# ]
allConstruct2('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])
# [] 
allConstruct2('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee'])
# [] 


def allConstruct3(target, wordBank):
    table = [[] for i in range(len(target) + 1)]
    table[0] = [[]]
    
    for i in range(len(target)):
        for word in wordBank:
            if word == target[i:(i + len(word))]:
                for arr in table[i]:
                    tempArr = arr[:]
                    tempArr.append(word)
                    table[i+len(word)].append(tempArr[:])
    
    return table[len(target)]


allConstruct3('purple', ['purpl', 'p', 'ur', 'le', 'purp']) 
# [ 
#   ['purp', 'le'],
#   ['p', 'ur',  'p' , 'le']
# ]
allConstruct3('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']) 
# [ 
#   ['ab', 'cd', 'ef'],
#   ['ab', 'c', 'def'],
#   ['abc', 'def'],
#   ['abcd', 'ef']
# ]
allConstruct3('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])
# [] 
allConstruct3('eeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeee', 'eeeeee']) # Using tabulation this takes longer 
# [] 

