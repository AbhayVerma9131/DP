from asyncio.windows_events import NULL


def howSum(targetSum,numbers,memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum ==0:
        return []
    if targetSum<0:
        return NULL
    for num in numbers:
        rem=targetSum-num
        remres=howSum(rem,numbers,memo)
        if (remres != NULL):
            memo[targetSum]=[*remres,num]
            return memo[targetSum]
            
    
    memo[targetSum]=NULL
    return NULL
        
        
        
print(howSum(300,[7,14]))