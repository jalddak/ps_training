import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

import heapq
heap = [(0, 1)]
visited = set([])
result = 0
while len(visited) < N:
    cost, node = heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)
    result += cost
    for e_node, e_cost in edges[node]:
        if e_node in visited:
            continue
        heapq.heappush(heap, (e_cost, e_node))
    
print(result)