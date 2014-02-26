def isPandigital(num):
    flag = True
    if len(str(num)) == 9:
        for x in range(1,10):
            if str(x) not in str(num):
                flag = False
                break
    else:
        flag=False
    return flag

total = 0
panArr = []
for m in range(2,101):
    for n in range(123 if m > 9 else 1234,int(10000/m)+1):
        prod = m*n
        if isPandigital(str(prod) + str(m)+str(n)):
            if(prod not in panArr):
                panArr.append(prod)
            print (m,n,prod)
print(sum(panArr))
