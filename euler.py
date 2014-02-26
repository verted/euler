import math

def isPali(string):
    return str(string) == str(string)[::-1]

def primeGen(max):
    allNums = [1 for i in range(max)]
    prime = []
    allNums[0] = 0
    allNums[1] = 0
    for i in range(2, int(math.sqrt(max) + 1)):
        if allNums[i] != 0:
            temp = int(math.pow(i, 2))
            while temp < max:
                allNums[temp] = 0
                temp += i
    return allNums

def isPandigital(num):
    strNum = str(num)
    flag = True
    for x in range(1, len(strNum)+1):
        if str(x) not in strNum:
            flag = False
    return flag
    
def isPrime(num):
    for x in range(1, int(math.sqrt(num))):
        if num%x==0:
            return False
    return True
def isPentagon(num):
    penTest = (math.sqrt(1 + 24*num) +1)/6
    return penTest == int(penTest)

def isTriangle(num):
    triTest = (math.sqrt(1 + 8*num) - 1)/2
    return triTest == int(triTest)

def isHexagonal(num):
    hexTest = (math.sqrt(1+8*num) +1)/4
    return hexTest == int(hexTest)

def isPermutation(n1, n2):
    list1 = [int(x) for x in str(n1)]
    list2 = [int(x) for x in str(n2)]
    return sorted(list1) == sorted(list2)

def comb(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

def isLychrel(num):
    i = 0
    while i < 50:
        s = num + int(str(num)[::-1])
        if isPali(s):
            return False
        i+=1
    return True
