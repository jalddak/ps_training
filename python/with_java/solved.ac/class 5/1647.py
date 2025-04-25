import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [{} for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if b not in edges[a] or edges[a][b] > c:
        edges[a][b] = c
    if a not in edges[b] or edges[b][a] > c:
        edges[b][a] = c

visited = set()

import heapq
heap = [(0, 1)]
answer = 0
maxCost = 0

while heap and len(visited) < n:
    cost, node = heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)
    answer += cost
    maxCost = max(cost, maxCost)

    for nNode in edges[node]:
        nCost = edges[node][nNode]
        if nNode in visited:
            continue
        heapq.heappush(heap, (nCost, nNode))

answer -= maxCost
print(answer)