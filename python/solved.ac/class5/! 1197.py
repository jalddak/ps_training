# 양방향이면 양쪽에 넣어줘야지

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = [[] for _ in range(V)]
for _ in range(E):
    d, a, cost = map(int, input().split())
    edges[d-1].append([a-1, cost])
    edges[a-1].append([d-1, cost])

import heapq
heap = [(0, 0)]
visited = set()
result = 0

while len(visited) < V:
    cost, node = heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)
    result += cost
    for n_node, n_cost in edges[node]:
        if n_node in visited:
            continue
        heapq.heappush(heap, (n_cost, n_node))

print(result)