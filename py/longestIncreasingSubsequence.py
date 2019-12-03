# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

def longest_increasing_subsequence(arr):

    # there is some relation to max of current or current + 1?

    # manual calc is a linear operation, iterate, and +1 to count each time bigger value is seen
    # def calcLinear(subNums):
    #     tempCount = 0
    #     # if second is smaller, don't even bother
    #     if len(subNums) > 1:
    #         if subNums[0] > subNums[1]:
    #             return 0
    #         else:
    #             for index in range(len(subNums)):
    #                 if index < len(subNums) - 1 and subNums[index] < subNums[index+1]:
    #                     tempCount += 1
    #             return tempCount
    #     else:
    #         return 1


    # num in nums
    #   maxCount = max(existing, calc(num))

    # for index in range(len(nums)):
    #     maxCount = max(maxCount, calcLinear(nums[index:]))

    
    # round 2
    # now I'm thinking of somehow maintaining biggest last item
    # I can do that in a separate structure so when I get to 18 I will have [2, 3, 7, 101] now I can add 18 there
    # so at that junction then I have a decision, if 18 is smaller than last, I can replace it
    # if it's bigger, I append to the list

    



result = longest_increasing_subsequence([10,9,2,5,3,7,101,18])
print('hi')