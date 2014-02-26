import sys
import os

input = sys.stdin.read()
input = input.replace("\n", "")
max = 0
for i in range(4,len(input)):
    res = int(input[i]) * int(input[i-1]) *int(input[i-2]) * int(input[i-3]) * int(input[i-4])  
    if res > max:
        max = res
print(max)
