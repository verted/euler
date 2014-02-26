import euler
x = 100
while True:
    x += 1
    flag = True
    for multi in range(2,7):
        if not euler.isPermutation(x, x * multi):
            flag = False
            break
    if flag:
        print(x)
        break
