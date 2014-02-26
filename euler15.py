gridSize = 
def traverse(grid, i, j):
    if i == gridSize and j == gridSize:
        return 1;
    if grid[i][j] == 0:
        if(i!=gridSize):
            grid[i][j] += traverse(grid, i+1, j)
        if(j!=gridSize):
            grid[i][j] += traverse(grid, i, j+1)
        return grid[i][j]
    else:
        return grid[i][j]


grid = [[0]*(gridSize+1) for i in range(gridSize+1)]
print(traverse(grid, 0,0))
