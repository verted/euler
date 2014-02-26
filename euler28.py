currNum = 1
currDim = 3
sumOfDiag = 1
while currDim <= 1001:
    for i in range(4):
        currNum += (currDim -1)
        sumOfDiag += currNum
    currDim += 2
print(sumOfDiag)
