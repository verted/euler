import sys
matrix = sys.stdin.read()
matrix = matrix.rstrip('\n').split('\n')
matrix = [row.split('\t') for row in matrix]
for row in matrix:
    for i in range(len(row)):
        row[i] = int(row[i])
for x in range(1, len(matrix)):
    matrix[0][x] += matrix[0][x-1]
    matrix[x][0] += matrix[x-1][0]
for x in range(1, len(matrix)):
    for y in range(1, len(matrix[x])):
        if matrix[x-1][y] > matrix[x][y-1]:
            matrix[x][y]+= matrix[x-1][y]
        else:
            matrix[x][y]+= matrix[x][y-1]
for x in matrix:
    print(x)
