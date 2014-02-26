import euler
primeTest = euler.primeGen(10000)
primeList = [x for x in range(len(primeTest)) if primeTest[x] and x > 1000]
for i1 in range(len(primeList)-1):
    for i2 in range(i1+1, len(primeList)):
        m = primeList[i1]
        n = primeList[i2]
        l = n + (n - m)
        if l < 10000 and primeTest[l]:
            if euler.isPermutation(m,n) and euler.isPermutation(m,l):
                print(m,n,l)
