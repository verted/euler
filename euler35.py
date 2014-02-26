import primeGenerator
primeTest = primeGenerator.gen(1000000)
primes = [i for i in range(len(primeTest)) if primeTest[i]]
circPrimes = []
for prime in primes:
    currPrime = prime
    primeFlag = True
    for x in range(len(str(prime))-1):
        currPrime = int(str(prime)[x+1:] + str(prime)[:x+1])
        if not primeTest[currPrime]:
            primeFlag = False
    if primeFlag:
        print(prime)
        circPrimes.append(prime)
print(len(circPrimes), circPrimes)
