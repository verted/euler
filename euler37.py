import primeGenerator
primeTest = primeGenerator.gen(1000000)
primes = [i for i in range(len(primeTest)) if primeTest[i]]
trunPrimes = []
for prime in primes:
    if prime < 11:
        continue
    flag = True
    currPrime = prime
    while currPrime > 0:
        if not primeTest[currPrime]:
            flag = False
        currPrime = int(currPrime/10)
    currPrime = prime
    while len(str(currPrime)) > 1:
        currPrime = int(str(currPrime)[1:])
        if not primeTest[currPrime]:
            flag = False
    if flag:
        trunPrimes.append(prime)
print(trunPrimes, sum(trunPrimes))
