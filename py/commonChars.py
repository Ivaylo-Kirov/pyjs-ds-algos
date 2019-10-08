
import math

def commonChars(A):
    AMap = dict()
    #AMapF = dict()
    listResult = []
    
    for ch in set(A[0]): # this is a cool trick for 'each unique item'
        AMap[ch] = A[0].count(ch)
    
    # for all remaining words now.. run counts of each..and if 0, then pop..otherwise add min to results
    for i in range(1, len(A)):
        for ch in set(A[0]):
            if ch in AMap:
                if ch in A[i]:
                    localCount = A[i].count(ch)
                    #AMapF[ch] = ch * min(localCount, AMap[ch])
                    AMap[ch] = min(localCount, AMap[ch])
                else:
                    if ch in AMap:
                        AMap.pop(ch)

    for ch in AMap:
        for i in range(0, AMap[ch]):
            listResult.append(ch)
    
    return listResult
    


result = commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"])
print('hi')