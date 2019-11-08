# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

# Example
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climbStairs(n):
    cache = [-1] * n
    def _climbStairs(n, current):
        if n == current:
            return 0
        if n - current == 1:
            return 1
        if n - current == 2:
            return 2
        if cache[current] != -1:
            return cache[current]
        else:
            cache[current] = _climbStairs(n, current + 1) + _climbStairs(n, current + 2)
            return cache[current]

    result = _climbStairs(n, 0)
    return result

result = climbStairs(5)
print('hi')

# imagine you are on the last steps, where you can manually calculate the result
# that ends up being your base case, and from there you just add those numbers down, similar to fibonacci
# 1 + 2 manual
# next step down made 2 recursive calls... first one returned 1, second one returned 2...
# the result is 3, stack gets popped, and remaining stairs below now can do their sum as well