# Given an array of integers nums, write a method that returns the "pivot" index of this array.

# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

# Example 1:

# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.


def pivotIndex(nums):
    if len(nums) == 0:
        return -1
    # calculate sums from L and R
    L = [0] * len(nums)
    R = [0] * len(nums)
    L[0] = nums[0]
    R[-1] = nums[-1]
    for i in range(1, len(nums)):
        L[i] = L[i-1] + nums[i]
    for i in range(len(nums)-2, -1, -1):
        R[i] = R[i+1] + nums[i]

    # compare results on each index
    for i in range(len(nums)):
        if L[i] == R[i]:
            return i
            # if results match, that's your pivot
    # ensure comparison starts from the left so that leftmost match is returned

    # if no match, return -1
    return -1
    
    # complexity should be linear, as we pass through nums, 3 times

result = pivotIndex([1, 7, 3, 6, 5, 6])
print('hi')