def islandPerimeter(grid):
    perimeter = 0
    for i, line in enumerate(grid):
        for j, block in enumerate(line):
            if block == 1:
                # left
                if j == 0 or j > 0 and line[j-1] == 0: # need OR it's a wall
                    perimeter += 1
                # right
                if j == len(line) - 1 or j < len(line) and line[j+1] == 0:
                    perimeter += 1
                # bottom?
                if i == len(grid) - 1 or i < len(grid) - 1 and grid[i+1][j] == 0:
                    perimeter += 1
                # top
                if i == 0 or i > 0 and grid[i-1][j] == 0:
                    perimeter += 1

                # how many sides are open? # for each side, add 1 to perimeter

    return perimeter


result = islandPerimeter([[0,1,0,0],
                          [1,1,1,0],
                          [0,1,0,0],
                          [1,1,0,0]])