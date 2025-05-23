f, s, g, u, d = map(int, input().split())

from collections import deque
q = deque([(s, 0)])

visited = [False for _ in range(f+1)]
visited[s] = True

result = -1
while q:
    x, cnt = q.popleft()
    if x == g:
        result = cnt
        break
    if x + u <= f and not visited[x+u]:
        visited[x+u] = True
        q.append((x+u, cnt+1))
    if x - d > 0 and not visited[x-d]:
        visited[x-d] = True
        q.append((x-d, cnt+1))

if result == -1:
    print("use the stairs")
else:
    print(result)