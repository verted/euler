result = 0
pow5={}
for i in range(10):
    pow5[i] = i **5
for i in range(2, 355000):
    sumOfPowers = 0
    number = i
    while number > 0:
        d = number%10
        number = int(number/10)
        sumOfPowers += pow5[d]
        
    if sumOfPowers == i:
        result+=i
        print(i)
print(result)
