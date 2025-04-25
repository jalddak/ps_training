import sys
input = sys.stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

visited = [False for _ in range(n+1)]
visited[1] = True

from collections import deque

q = deque([1])
answer = [-1 for _ in range(n+1)]

while q:
    node = q.popleft()
    for nextNode in edges[node]:
        if not visited[nextNode]:
            visited[nextNode] = True
            q.append(nextNode)
            answer[nextNode] = node

for i in range(2, n+1):
    print(answer[i])