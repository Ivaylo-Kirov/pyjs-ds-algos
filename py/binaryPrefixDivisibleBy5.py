# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

# Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

# Example 1:

# Input: [0,1,1]
# Output: [true,false,false]
# Explanation: 
# The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

def prefixesDivBy5(A):
    result = []

    # iterate and grab from 0 to current index
    # now join into str
    # represent that str of binary digits as a real digit
    # return % 5 == 0 inside result.append
    
    As = [str(cur) for cur in A]
    
    for i in range(1, len(A)+1):
        curInt = int(''.join(As[:i]), 2)
        res = curInt % 5
        result.append(res == 0)

    return result


result = prefixesDivBy5([0, 1, 1])
print('hi')