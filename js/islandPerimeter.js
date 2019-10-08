
function islandPerimeter(grid){
    let perimeter = 0

    for (let i = 0; i < grid.length; ++i){
        for (let j = 0; j < grid[0].length; ++j){
            if (grid[i][j] == 1){
                // left
                if (j == 0 || j > 0 && grid[i][j-1] == 0){ // need || it's a wall
                    perimeter += 1
                }
                // right
                if (j == grid[i].length - 1 || j < grid[i].length - 1 && grid[i][j+1] == 0){
                    perimeter += 1
                }
                // bottom?
                if (i == grid.length - 1 || i < grid.length - 1 && grid[i+1][j] == 0){
                    perimeter += 1
                }
                // if i == len(grid) - 1 or i < len(grid) - 1 and grid[i+1][j] == 0:
                // top
                if (i == 0 || i > 0 && grid[i-1][j] == 0){
                    perimeter += 1
                }
                // how many sides are open? // f|| each side, add 1 to perimeter
            }
        }
    
    }
    return perimeter
}

const result = islandPerimeter([[1], [0]]);