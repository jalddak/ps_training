import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list((map(int, input().split())))
    nums = deque(p)
    p.sort()

    cnt = 0
    while(m >= 0):
        num = nums.popleft()
        m -= 1
        if num == p[-1]:
            p.pop()
            cnt += 1
        else:
            nums.append(num)
            m = len(nums)-1 if m == -1 else m
    
    print(cnt)

