# Given an array A of integers, return true if and only if it is a valid mountain array.

# Recall that A is a mountain array if and only if:

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

# Example 1:

# Input: [2,1]
# Output: false
# Example 2:

# Input: [3,5,5]
# Output: false
# Example 3:

# Input: [0,3,2,1]
# Output: true

# to be less confusing, this should be called a "triangle" because it's not really about it being a mountain, it requires constant pointing up


def validMountainArray(A):
    if len(A) < 3:
        return False
    L, R = [False] * len(A), [False] * len(A)

    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            L[i] = True
            if i == 1:
                L[0] = True

    for i in range(len(A) - 2, -1, -1):
        if A[i] > A[i+1]:
            R[i] = True
            if i == len(A) - 2:
                R[len(A) - 1] = True

    if L[0] == False or R[-1] == False:
        return False

    # now if my calculations are correct, if we ever see False for both, then it's not a mountain
    for i in range(len(A)):
        if L[i] == False and R[i] == False:
            return False
    
    return True

result = validMountainArray([0,1,2,3,4,5,6,7,8,9])
print('hi')