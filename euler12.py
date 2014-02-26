import math
num = 0
triNum = 0
found = 0
while not found:
    num += 1
    triNum += num
    temp = 1
    numDivisor = 0
    while temp < math.sqrt(triNum):
        if triNum % temp ==0:
            if triNum/temp == temp:
                numDivisor += 1
            else:
                numDivisor += 2
        temp+=1
    if numDivisor > 500:
        found = 1
print(num, triNum)
    
