import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())

edges = dict()
for _ in range(e):
    s, e, w = map(int, input().split())
    if s not in edges:
        edges[s] = {e : w}
    elif e not in edges[s] or edges[s][e] > w:
        edges[s][e] = w

import heapq
heap = [(0, k)]
checked = [20000 * 10 + 1 for _ in range(v+1)]
checked[k] = 0


while heap:
    cost, x = heapq.heappop(heap)
    if cost > checked[x] or x not in edges: continue
    for nx in edges[x]:
        nCost = cost + edges[x][nx]
        if nCost >= checked[nx]:
            continue
        checked[nx] = nCost
        heapq.heappush(heap, (nCost, nx))

for i in range(1, v+1):
    c = checked[i]
    if c == 20000 * 10 + 1:
        c = "INF"
    print(c)