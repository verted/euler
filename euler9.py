import math
found = 0
c = 998
while not found:
    c-=1
    a=1
    b=1000-c-a
    if b > c:
        b = c-1
        a = 1000- b - c
    while a < b:
        if math.pow(a,2) + math.pow(b,2) == math.pow(c, 2):
            found = 1
            break
        else:
            a+=1
            b-=1
    
print(a, b, c)
