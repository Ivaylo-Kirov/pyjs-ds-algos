# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

 

# Example 1:

# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:

# Input: 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    
    result = 0

    while n:
        result += n & 1
        n >>= 1

    return result


result = hammingWeight(7)
print('hi')

