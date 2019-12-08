# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

# Example 1:

# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

def shortestToChar(S, C):
    result = [1000000] * len(S)
    L = [1000000] * len(S)
    R = [1000000] * len(S)

    L[0] = 0 if S[0] == C else 1000000
    R[-1] = 0 if S[-1] == C else 1000000

    for i in range(1, len(S)):
        if S[i] == C:
            L[i] = 0
        else:
            L[i] = L[i-1] + 1
    
    for i in range(len(S) - 2, -1, -1):
        if S[i] == C:
            R[i] = 0
        else:
            R[i] = R[i+1] + 1
    
    for i in range(len(S)):
        result[i] = min(L[i], R[i])

    return result

result = shortestToChar("loveleetcode", "e")
print('h')