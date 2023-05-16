import re

def canConstruct(target,worldBank,memo={}):
    if target =='':
        return True
    for word in worldBank:
        if target.index(word)==0:
            suffix=target[slice(len(word),len(target))]
            res=canConstruct(suffix,worldBank)
            if (res==True):
                return True
    return False

print(canConstruct("abhay",["ab","h","hay","abh"]))            