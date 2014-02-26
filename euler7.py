import math

max = 1000000
allNums = [i for i in range(max)]
prime = []
allNums[0] = 0
allNums[1] = 0
for i in range(2, int(math.sqrt(max) + 1)):
    if allNums[i] != 0:
        temp = int(math.pow(i, 2))
        while temp < max:
            allNums[temp] = 0
            temp += i
primes = [i for i in allNums if i!=0]
print (primes[10000])
