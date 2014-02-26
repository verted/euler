import euler, math
primeTest = euler.primeGen(1000000)
primes = [x for x in range(len(primeTest)) if primeTest[x]]
def numOfDistinctPrimes(num):
    i = 0
    count = 0
    origNum = num
    while(num > 1):
        flag = False
        while num % primes[i] == 0:
            flag=True
            num = num/primes[i]
        if flag:
            count +=1
        i += 1
    print(origNum, count)
    return count

numList = [0, 1]
for x in range(2, 1000000):
    numList.append(numOfDistinctPrimes(x))
    if len(numList) >= 4:
        if numList[-1] == 4 and numList[-2] == 4 and numList[-3] == 4 and numList[-4] == 4:
            break
print(numList[-4])
