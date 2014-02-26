import math

def primeGen(max):
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
    for num in allNums:
        if num != 0:
            prime.append(num)
    return prime

b = 10
for p in primeGen(1000):
    if b % p != 0:
        t = 0
        r = 1
        n = 0
        while True:
            t += 1
            x = r*b
            d = int(x/p)
            r = x % p
            n = n*b+d
            if r == 1:
                break
        if t == p -1:
            print(p, 1/p)
