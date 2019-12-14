# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2
import math
def majorityElement(nums):

    # dict with counts
    nDict = dict()
    for num in nums:
        if num in nDict:
            nDict[num] += 1
        else:
            nDict[num] = 1
        
    # iterate dict, and when you find the value equal to len(nums) / 2, return it
    for k, v in nDict.items():
        if v >= math.ceil(len(nums) / 2):
            return k


result = majorityElement([3,2,3])
print('hi')