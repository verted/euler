import math
divisorSums = {}
for i in range(2,10000):
    factor = 2
    currDivisorSum = 1
    while factor < math.sqrt(i):
        if i % factor == 0:
            currDivisorSum += factor + i/factor
        factor+=1
    divisorSums[i] = currDivisorSum
aPairs = [x for x in divisorSums.keys() if divisorSums[x] in divisorSums and divisorSums[divisorSums[x]]==x and divisorSums[x] != x]
print(sum(aPairs))
