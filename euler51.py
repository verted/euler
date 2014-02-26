import primeGenerator

primeTest = primeGenerator.gen(150000000)
numOnDiag = 1
numPrimes = 0
dim = 0
num = 1 
while numPrimes/numOnDiag > 0.10 or numPrimes == 0:
    dim += 2
    for i in range(4):
        num+= dim
        numPrimes += primeTest[num]
    numOnDiag += 4
    print(numPrimes, numOnDiag, numPrimes/numOnDiag, dim)
print(dim)
