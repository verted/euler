import math
import datetime

numbers = [0,1,2,3,4,5,6,7,8,9]
numPerm = 1000000
perm = ""
numbersRemaining = len(numbers)
for currFac in reversed(range(10)):
    for i in range(len(numbers)):
        if (i+1)*math.factorial(currFac) >= numPerm:
            numPerm -= (i)*math.factorial(currFac)
            perm += str(numbers[i])
            del numbers[i]
            break
print(perm)
    
