# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# Example 1:

# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

def canJump(nums):

    # my ideas are around trying all possibilities

    # at index 0 try both (i.e. investigate(1) investigate(2))

    def investigate(index, numsc):
        if numsc[index] == 0:
            return False
        elif len(numsc) - (index + numsc[index]) <= 1:
            return True
        
        for i in range(numsc[index]):
            return investigate(index + i + 1, numsc)

    # now do checks to see if I reached the end
    # if not, keep investigating forward based on available jumps

    # some memoization possiblitiy here is to not investigate index I've already tried
    return investigate(0, nums)

result = canJump([2,3,1,1,4])
print('hi')
