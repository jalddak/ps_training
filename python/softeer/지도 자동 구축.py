import sys

n = int(input())

result = 4

# 1 2 2 1
# 2 3 2 4
# 4 5 2 16
# 8 9 2 32

for i in range(n):
    result += ((2**i) * (2**i+1) * 2 )+ (4 ** i)

print(result)