n, k = map(int, input().split())

visited = [100001 for _ in range(100001)]
visited[n] = 0

from collections import deque
q = deque([n])

result = 100001
while q:
    x = q.popleft()
    if x == k:
        result = min(result, visited[x])
    if x-1 >= 0 and visited[x-1] > visited[x] + 1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if x+1 < 100001 and visited[x+1] > visited[x] + 1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
    if 2*x < 100001 and visited[2*x] > visited[x]:
        visited[2*x] = visited[x]
        q.append(2*x)

print(result)