import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edges = {}
for _ in range(m):
    s, e, cost = map(int, input().split())
    if s not in edges:
        edges[s] = {e : cost}
    if e not in edges[s] or edges[s][e] > cost:
        edges[s][e] = cost

s, e = map(int, input().split())
costs = [100000 * n + 1 for _ in range(n+1)]
costs[s] = 0
parents = [0 for _ in range(n+1)]

import heapq
heap = [(0, s)]

while heap:
    cost, x = heapq.heappop(heap)
    if x == e:
        break
    if cost < costs[x] or x not in edges:
        continue
    for nx in edges[x]:
        nCost = cost + edges[x][nx]
        if costs[nx] <= nCost:
            continue
        costs[nx] = nCost
        parents[nx] = x
        heapq.heappush(heap, (nCost, nx))

result = [e]
while parents[result[-1]] != 0:
    result.append(parents[result[-1]])

print(costs[e])
print(len(result))
print(" ".join(map(str, reversed(result))))