# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

def uniquePaths(m, n):

    # m / n is the grid, using example, let's say it's 7 and 3

    def countPath(locx, locy):
        if locx == m or locy == n:
            return 0
        else:
            return countPath(locx+1, locy) + countPath(locx, locy+1) + 1
    
    return countPath(1, 1) + 1

# next step is memoization but I gave up
result = uniquePaths(7, 3)
print('hi')