import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

import heapq
heap = [(0, 1)]

visited = [False for _ in range(v+1)]
answer = 0

while heap:
    cost, node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    answer += cost
    for nNode, nCost in edges[node]:
        if visited[nNode]:
            continue
        heapq.heappush(heap, (nCost, nNode))

print(answer)