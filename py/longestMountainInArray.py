# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 

# Return 0 if there is no mountain.

# Example 1:

# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.

def longestMountain(A):
    L = [0] * len(A)
    R = [0] * len(A)

    L[0] = 1
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            L[i] = L[i-1] + 1
        else:
            L[i] = 1
    
    R[-1] = 1
    for i in range(len(A)-2, 0, -1):
        if A[i] > A[i+1]:
            R[i] = R[i+1] + 1
        else:
            R[i] = 1

    maxCount = 0
    for i in range(len(A)):
        maxCount = max(maxCount, L[i] + R[i] - 1)
    
    return maxCount if maxCount >= 3 else 0

result = longestMountain([2,2, 2])
print('hi')