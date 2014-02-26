import sys
input = sys.stdin.read()
input = input.rstrip()
tri = input.split("\n")
triOrig = list(tri)
for i in range(len(tri)):
    tri[i] = [[int(x)] for x in tri[i].split(" ")]
for i in range(len(triOrig)):
    triOrig[i] = triOrig[i].split(" ")
tri[0][0].append([[0,0]])
for i in range(1, len(tri)):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][j][0] += tri[i-1][j][0]
            tri[i][j].append(list(tri[i-1][j][1]))
        elif j == len(tri[i]) - 1:
            tri[i][j][0] += tri[i-1][j-1][0]
            tri[i][j].append(list(tri[i-1][j-1][1]))
        else:
            tri[i][j][0] += max(tri[i-1][j-1][0], tri[i-1][j][0])
            if(tri[i-1][j-1][0]> tri[i-1][j][0]):
                tri[i][j].append(list(tri[i-1][j-1][1]))
            else:
                tri[i][j].append(list(tri[i-1][j][1]))
        tri[i][j][1].append([i, j])
print (max(tri[len(tri)-1]))
for coord in max(tri[len(tri)-1])[1]:
    print (triOrig[coord[0]][coord[1]])
