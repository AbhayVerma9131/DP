import string


def grideTravel(m,n,memo={}):
    key=str(m)+', '+str(n)
    if key in memo:
        return memo[key]
    if m==0 or n==0:
        return 0
    if m==1 or n==1:
        return 1
    memo[key]= grideTravel(m,n-1,memo)+grideTravel(m-1,n,memo)
    return memo[key]

print(grideTravel(18,18))