from collections import deque

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]

visited[n] = n
q = deque([n])

while q:
    x = q.popleft()
    if x == k:
        break
    if x-1 >= 0 and visited[x-1] == -1:
        visited[x-1] = x
        q.append(x-1)
    if x+1 <= 100000 and visited[x+1] == -1:
        visited[x+1] = x
        q.append(x+1)
    if 2*x <= 100000 and visited[2*x] == -1:
        visited[2*x] = x
        q.append(2*x)

x = k
result = []
while visited[x] != x:
    result.append(x)
    x = visited[x]
result.append(n)
print(len(result)-1)
result.reverse()
print(" ".join(map(str, result)))