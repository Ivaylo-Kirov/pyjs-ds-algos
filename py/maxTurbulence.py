# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# Return the length of a maximum size turbulent subarray of A.

# Example 1:

# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:

# Input: [4,8,12,16]
# Output: 2
# Example 3:

# Input: [100]
# Output: 1

def maxTurbulenceSize(A):
    dp = [0] * len(A)
    dp[-1] = 1

    for i in range(len(A) - 2, -1, -1):
        if i % 2 == 0:
            # even index - what is the rule?
            dp[i] = dp[i+1] + 1 if A[i] < A[i+1] else 1
        else:
            # odd index - what is the rule?
            dp[i] = dp[i+1] + 1 if A[i] > A[i+1] else 1

    return max(dp)

# seems to work for the most part, but one weird test case with 0s and 1s throws it off (might be broken)
# learning here is maintaining a DP array and incrementing value based on success condition

result = maxTurbulenceSize([4,8,12,16])
print('hi')