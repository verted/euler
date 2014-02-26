result = 0
resultSolution = 0
p = 2
while p <= 1000:
    numberOfSolutions = 0
    for a in range(2,int(p/3)):
        if (p*(p-2*a) % (2*(p-a)) )==0:
            numberOfSolutions+=1
    if numberOfSolutions > resultSolution:
        resultSolution = numberOfSolutions
        result = p
    p+=2
print(result)
