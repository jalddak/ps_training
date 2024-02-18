import sys

n = int(input())

lengths = list(map(int, input().split()))

prime_nums = [False] * 2 + [True] * 99
pnd = {}
for i in range(101):
    if prime_nums[i] == True:
        pnd[i] = 0
        for j in range(2*i, 101, i):
            prime_nums[j] = False

prime_nums = list(pnd.keys())

for l in lengths:
    for num in prime_nums:
        if num > l:
            break
        if l % num == 0:
            pnd[num] += 1

print(max(pnd.values()))
