import primeGenerator
import time
start_time = time.time()
prime = primeGenerator.generatePrimes(5000000)
print (time.time() - start_time, "seconds")
primeSum = 0
maxNum = 0
for num in prime:
    primeSum += num
    maxNum += 1
    if primeSum > 5000000:
        primeSum -= num
        maxNum -= 1
        break
print(primeSum, maxNum)
for num in prime:
    if primeSum[prime]:
        break
    primeSum -= num
    maxNum -=1
print(primeSum, maxNum)

