# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false

# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

def canThreePartsEqualSum(A):
    total = sum(A)

    if total % 3 != 0:
        return False
    
    target = int(total / 3)
    cur = 0
    i = 0
    total_targets_hit = 0
    while cur != target and total_targets_hit < 3 and i < len(A):
        cur += A[i]
        i += 1
        if cur == target:
            total_targets_hit += 1
            cur = 0
    
    if total_targets_hit < 3:
        return False

    return True


result = canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
print('hi')