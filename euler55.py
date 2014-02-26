import euler
lychrelList = {}
def isLychrel(num):
    i = 0
    numList = []
    flag = True
    while i < 50:
        if num in lychrelList.keys():
            flag = lychrelList[num]
            break
        numList.append(num)
        s = num + int(str(num)[::-1])
        if euler.isPali(s):
            flag = False
            break
        num = s
        i+=1
    for temp in numList:
        lychrelList[temp] = flag
    return flag

count = 0
for i in range(10, 10000):
    if isLychrel(i):
        count += 1
print(count)
