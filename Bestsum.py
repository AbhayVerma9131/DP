from asyncio.windows_events import NULL
from re import T


def bestSum(targetSum,number,memo={}):
    
    if targetSum in memo:
        return memo[targetSum]
    if targetSum==0:
        return []
    if targetSum<0:
        return NULL
    
    short=NULL
    for num in number:
        rem=targetSum-num
        remres=bestSum(rem,number,memo)
        if remres!=NULL:
            comb=[*remres,num]
            if (short==NULL or len(short)<len(comb)):
                short=comb
                memo[targetSum]=short
                return short
            
print(bestSum(100,[10,5,2,1]))            
