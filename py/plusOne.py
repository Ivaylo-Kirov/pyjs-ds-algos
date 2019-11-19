# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plusOne(digits):
    end = len(digits) - 1

    while digits[end] == 9:
        digits[end] = 0
        end -= 1
    
    if end < 0:
        digits.insert(0, 1)
    else:
        digits[end] += 1

    return digits

result = plusOne([9, 9])
print('hi')
