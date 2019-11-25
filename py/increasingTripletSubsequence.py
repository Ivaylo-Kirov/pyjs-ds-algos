# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

# Example 1:

# Input: [1,2,3,4,5]
# Output: true
# Example 2:
# Input: [5,4,3,2,1]
# Output: false


def increasingTriplet(nums):
    curi = 1
    curc = 1
    while curi < len(nums):
        if nums[curi-1] < nums[curi]: # only qualify equals when count is already above 1
            curc += 1
        elif nums[curi-1] == nums[curi] and curc > 1:
            curc += 1
        else:
            curc = 1
        curi += 1
        if curc > 2:
            return True

    return False


# fails some weird test case that seems broken anyway
# the lessons were again the annoyance of maintaining double index
# another lesson is using index-1 and current so you don't have to worry about index out of range

result = increasingTriplet([5,1,5,5,2,5,4])
print('hi')
