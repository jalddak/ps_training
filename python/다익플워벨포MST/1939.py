import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
bridge = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    bridge[a].append((-c, b))
    bridge[b].append((-c, a))

s, e = map(int, input().split())

import heapq
heap = [(-1000000000, s)]

while heap:
    cost, node = heapq.heappop(heap)
    visited[node] = True
    if node == e:
        print(-cost)
        exit()
    for n_cost, n_node in bridge[node]:
        if not visited[n_node]:
            heapq.heappush(heap, (max(cost, n_cost), n_node))