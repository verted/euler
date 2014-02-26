numbers = {1:"one",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6:"six",
           7:"seven",
           8:"eight",
           9:"nine",
           10:"ten",
           11:"eleven",
           12:"twelve",
           13:"thirteen",
           14:"fourteen",
           15:"fifteen",
           16:"sixteen",
           17:"seventeen",
           18:"eighteen",
           19:"nineteen",
           20:"twenty",
           30:"thirty",
           40:"forty",
           50:"fifty",
           60:"sixty",
           70:"seventy",
           80:"eighty",
           90:"ninety"}
totalSum = 0
for i in range(1,1001):
    currNum = i
    currNumString = ""
    while currNum > 0:
        if currNum <= 20:
            currNumString += numbers[currNum]
            currNum = 0
        elif currNum < 100:
            currNumString += numbers[int(currNum/10)*10]
            currNum = currNum % 10
        elif currNum < 1000:
            print(currNum)
            currNumString += numbers[int(currNum/100)] + "hundred"
            currNum = currNum%100
            if currNum > 0:
                currNumString += "and"
        else:
            currNum = 0
            currNumString = "onethousand"
    print (currNumString)
    totalSum += len(currNumString)
print (totalSum)
