num1 = 1
num2 = 1
fibNum = 0
term = 2
while len(str(fibNum)) < 1000:
    fibNum = num1 + num2
    num1 = num2
    num2=fibNum
    term += 1
print (fibNum, term)
