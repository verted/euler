import math
def isAbundant(i):
    total = 0
    for x in range(1,int(math.sqrt(i)+1)):
        if i % x == 0:
            total += x
            if x != i/x and x != 1:
                total += i/x
    return total > i

limit = 28123
abundantNums = []
for i in range(1,limit+1):
    if isAbundant(i):
        abundantNums.append(i)
allNums = [0 for x in range(limit+1)]
print(len(abundantNums))
for x in range(len(abundantNums)):
    for y in range(x,len(abundantNums)):
        if abundantNums[x] + abundantNums[y] <= limit:
            allNums[abundantNums[x] + abundantNums[y]] = 1
        else:
            break
print(sum([x for x in range(len(allNums))if allNums[x] == 0]))

