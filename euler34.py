import math
def fact(temp):
    sum = 0
    for i in temp:
        sum+=math.factorial(int(i))
    return sum

total = 0
for i in range(3,9999999):
    if fact(str(i)) == i:
        total+=i
print(total)
