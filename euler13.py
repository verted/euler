import sys
input = sys.stdin.read()
input = input.rstrip()
number = input.split("\n")
total = 0
for num in number:
    total += int(num[:11])
print(total)
