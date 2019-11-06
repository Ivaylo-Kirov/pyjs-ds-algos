# https://leetcode.com/problems/number-of-islands/

def numIslands(grid):
    # looks like DFS
    # keep going while you can reach 1s, and add those 1s to visited hash
    # append 1 to numberOfIslands
    
    # keep recursing, check for visited, if not visited and it's 1, repeat above
    
    result = 0

    for i in range(5):
        for j in range(4):
            if _dfs(grid, i, j, 0) > 0:
                result += 1

    return result
    
    
def _dfs(grid, startX, startY, result, visited = set()):
    if str(f'{startX}{startY}') not in visited:
        visited.add(f'{startX}{startY}')
        if grid[startX][startY] == '0':
            return 0
        else:
            result += 1
            if startY + 1 < 4 and grid[startX][startY+1] == '1':
                return result + _dfs(grid, startX, startY + 1, result)
            elif startX + 1 < 5 and grid[startX+1][startY] == '1':
                return result + _dfs(grid, startX + 1, startY, result)
            elif startY - 1 > 0 and grid[startX][startY-1] == '1':
                return result + _dfs(grid, startX, startY - 1, result)
            elif startX - 1 > 0 and grid[startX-1][startY] == '1':
                return result + _dfs(grid, startX-1, startY, result)
            else:
                return 0
    else:
        return 0

result = numIslands([list('11110'), list('11010'), list('11000'), list('00000')])
# result = numIslands([list('10000'), list('00000'), list('00000'), list('00000')])
print('hi')
