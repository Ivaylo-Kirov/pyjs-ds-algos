# grid of boxes
# each box is R, G, or B
# find the max of connected boxes

def connectedComponents(grid):
    visited = set()

    def isvalid(i, j):
        if i >= len(grid) or i < 0:
            return False
        elif j >= len(grid[i]) or j < 0:
            return False
        return True

    # edge cases still being worked on.. maybe need an isvalid() method
    def dfs(i, j):
        if (i, j) in visited:
            return 0
        else:
            visited.add((i, j))
            result = 0
            cur = grid[i][j]
            # goal is to return some sort of INT result of consecutive matches
            if isvalid(i+1, j) and grid[i+1][j] == cur:
                result += dfs(i+1, j)
            if isvalid(i, j+1) and grid[i][j+1] == cur:
                result += dfs(i, j+1)
            if isvalid(i-1, j) and grid[i-1][j] == cur:
                result += dfs(i-1, j)
            if isvalid(i, j-1) and grid[i][j-1] == cur:
                result += dfs(i, j-1)
            # combine lengths of 4-directional dfs, and return that value + 1 to account for parent node
            return result + 1

    curMax = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            curMax = max(curMax, dfs(i, j))
    return curMax

result = connectedComponents([[0, 1, 1, 0], [2, 2, 1, 0], [0, 0, 1, 0]])
print('hi')