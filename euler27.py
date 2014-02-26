import primeGenerator
bList = primeGenerator.gen(1000)
bList = [x for x in range(len(bList)) if bList[x] == 1]
primeTest = primeGenerator.gen(2000000)
nMax = 0
aMax = 0
bMax = 0
for a in range(-999,1000):
    for b in bList:
        n = 0
        while primeTest[n**2 + a*n +b]:
            n+=1
        if n >nMax:
            aMax = a
            bMax = b
            nMax = n
print(aMax,bMax,aMax*bMax,nMax)
