import math
sumOfSquares = sum([math.pow(i, 2) for i in range(1, 101)])
print(sum(list(range(1, 101))))
squareOfSum = math.pow(sum(list(range(1, 101))),2)
print(squareOfSum - sumOfSquares)
    
