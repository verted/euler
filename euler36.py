def isPali(string):
    pali = True
    for i in range(int(len(string)/2)):
        if string[i] != string[-i-1]:
            pali = False
    return pali

total = 0
for x in range(1000000):
    if isPali(str(x)) and isPali(bin(x)[2:]):
        total+= x
print(total)
