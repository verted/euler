digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
largestPDig = 0
largestI = 0
largestJ = 0
for i in range(10000):
    numString = ""
    j = 0
    while len(numString) < 9:
        j+=1
        numString += str(j*i)
    if len(numString) == 9:
        allDig = True
        for digit in digits:
            if digit not in numString:
                allDig = False
        if(allDig):
            print()
            for temp in range(1,j+1):
                print(i, "X", temp, "=", i * temp)
            print(numString)
        if allDig and largestPDig < int(numString):
            largestPDig = int(numString)
            largestI = i
            largestJ = j
print(largestPDig)
for j in range(1,largestJ+1):
    print(largestI, "X", j, "=", largestI * j)
    
