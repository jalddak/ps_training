n, k = map(int, input().split())

from collections import deque

q = deque([(n, 0)])
visited = [False for _ in range(100001)]
visited[n] = True

result = -1
while q:
    x, cnt = q.popleft()
    if x == k:
        result = cnt
        break
    if x - 1 >= 0 and not visited[x-1]:
        visited[x-1] = True
        q.append((x-1, cnt + 1))
    if x + 1 <= 100000 and not visited[x+1]:
        visited[x+1] = True
        q.append((x+1, cnt + 1))
    if 2 * x <= 100000 and not visited[2*x]:
        visited[2*x] = True
        q.append((2*x, cnt + 1))

print(result)