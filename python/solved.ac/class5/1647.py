import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append([B, C])
    edges[B].append([A, C])

import heapq
heap = [(0, 1)]
visited = set([])
result = []

while len(visited) < N:
    cost, house = heapq.heappop(heap)
    if house in visited:
        continue
    visited.add(house)
    result.append(cost)
    for next, n_cost in edges[house]:
        if next in visited:
            continue
        heapq.heappush(heap, (n_cost, next))

print(sum(result) - max(result))


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])

roots = [i for i in range(N+1)]

def find(n):
    global roots
    if roots[n] != n:
        roots[n] = find(roots[n])
    return roots[n]
    
result = 0
big_edge = 0
for s, e, c in edges:
    sroot = find(s)
    eroot = find(e)
    if sroot != eroot:
        if sroot < eroot:
            roots[eroot] = sroot
        else:
            roots[sroot] = eroot
        result += c
        big_edge = c
        print(result, big_edge)

print(result - big_edge)