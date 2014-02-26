import euler
i = 144
while(True):
    hexNum = i*(2*i -1)
    if euler.isPentagon(hexNum):
        print(hexNum)
        break
    i+=1
