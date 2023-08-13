# BFS

from collections import deque

A, B = list(map(int, input().split()))

queue = deque([[A, 1]])

result = -1
while len(queue) != 0:
    n, cnt = queue.popleft()
    if n == B:
        if result == -1:
            result = cnt
        else:
            result = min(result, cnt)
        continue
    strn = str(n)
    r1n = strn + '1'
    r1n = int(r1n)
    if 2*n <= B:
        queue.append([2*n, cnt+1])
    if r1n <= B:
        queue.append([r1n, cnt+1])
print(result)