import sys
def check(i, i1, i2, i3, maxProd):
    currProd = int(i) * int(i1) * int(i2) * int(i3)
    if currProd > maxProd:
        return currProd
    else:
        return maxProd


input = sys.stdin.read()
grid = input.rstrip().split("\n")
for i in range(0,len(grid)):
    grid[i] = grid[i].split()
maxHeight = len(grid)
maxLength = len(grid[0]) #assuming rows are all the same length
maxProd = 0
for i in range(maxHeight):
    for j in range(maxLength):
        checkDown = False
        checkRight = False
        if i + 3 < maxHeight:
            maxProd = check(grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j], maxProd)
            checkDown = True
        if j + 3 < maxLength:
            maxProd = check(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i][j+3], maxProd)
            checkRight = True
        if j -3 < maxLength and checkDown:
            maxProd = check(grid[i][j], grid[i+1][j-1], grid[i+2][j-2], grid[i+3][j-3], maxProd)
        if checkDown and checkRight:
            maxProd = check(grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3], maxProd)
    print (maxProd)
print (maxProd)
        
