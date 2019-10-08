
def removeDuplicates(S):
    madeRevisions = True
    
    while madeRevisions == True:
        madeRevisions = False
        for i in range(len(S)):
            if i < len(S) - 1 and S[i] == S[i+1]:
                madeRevisions = True
                S = S[:i] + S[i+2:]
                
    return S


result = removeDuplicates("abbacaddeegh")