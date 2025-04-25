a, b = map(int, input().split())

from collections import deque
q = deque([(a, 1)])

answer = -1
while q:
    n, cnt = q.popleft()
    if n == b:
        answer = cnt
        break
    if n * 2 > b and n * 10 + 1 > b:
        continue
    q.append((n * 2, cnt + 1))
    q.append((n * 10 + 1, cnt + 1))

print(answer)