import sys
from collections import deque

nums = ['1110111',
        '0010001',
        '0111110',
        '0111011',
        '1011001',
        '1101011',
        '1101111',
        '1110001',
        '1111111',
        '1111011',
        '0000000',
       ]

def check(a, b):
    cnt = 0
    for i in range(7):
        if a[i] != b[i]:
            cnt += 1
    return cnt
    
t = int(input())
answer = []
for _ in range(t):
    a, b = map(deque, input().split())
    short = a if len(a) < len(b) else b
    while len(a) != len(b):
        short.appendleft('-1')
    a = list(map(int, a))
    b = list(map(int, b))

    n = len(a)
    result = 0
    for i in range(n):
        if a[i] == b[i]:
            continue
        result += check(nums[a[i]], nums[b[i]])
    answer.append(result)

for n in answer:
    print(n)