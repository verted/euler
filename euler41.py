import euler
primes = euler.primeGen(7654321)
primeList = [x for x in range(len(primes)) if primes[x]]
for prime in reversed(primeList):
    print(prime)
    if euler.isPandigital(prime):
        break
print(prime)
    
