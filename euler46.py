import math, euler
primeTest = euler.primeGen(10000)
primes = [x for x in range(len(primeTest)) if primeTest[x]]
oddComps = [x for x in range(len(primeTest)) if not primeTest[x] and x % 2 and x > 3]
for oddComp in oddComps:
    flag = False
    for prime in primes:
        if oddComp > prime:
            temp = math.sqrt((oddComp - prime)/2)
            if temp == int(temp):
                flag = True
                break
        else:
            break
    if flag == False:
        print(oddComp)
        break
