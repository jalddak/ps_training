import sys

input = sys.stdin.readline

K, N = map(int, input().split())

lans = [int(input()) for _ in range(K)]
min_cm = 1
max_cm = max(lans)

while min_cm + 1 < max_cm:
    able = 0
    middle = (min_cm + max_cm) // 2
    for n in lans:
        able += n // middle
    if N > able:
        max_cm = middle
    elif N <= able:
        min_cm = middle

check = 0
for n in lans:
    check += n // max_cm
if N <= check:
    print(max_cm)
else: print(min_cm)