import euler, math
pentList = []
i = 1
found = False
while not found:
    currPent = i*(i*3 -1)/2
    for num in pentList:
        if euler.isPentagon(currPent + num) and euler.isPentagon(math.fabs(currPent - num)):
            print(currPent, num, math.fabs(currPent-num))
    pentList.append(currPent)
    i+=1

