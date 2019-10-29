class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        result = 0
        
        # increase each by as much as possible, and increment result with that value
        
        # List[0] = can easily get row0max = 8 
        # List[1] = can easily get row1max = 7 
        # List[2] = can easily get row2max = 9
        # List[3] = can easily get row3max = 3
        
        # List[0][0] # List[1][0] # List[2][0] # List[3][0] column0max = 9
        maxOfColumn = [0] * len(grid)
        
        for i in range(len(grid)):
            currentMax = 0
            for j in range(len(grid)):
                currentMax = max(currentMax, grid[j][i])
            maxOfColumn[i] = currentMax
                 
        # from the above, I can now determine that List[0][0] can become 8
        # but also that List[1][0] can become 7
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                current = grid[i][j]
                grid[i][j] = min(max(grid[i]), maxOfColumn[j])
                new = grid[i][j]
                result += new - current
        
        return result