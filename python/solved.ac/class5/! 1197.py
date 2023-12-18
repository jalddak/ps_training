# 양방향이면 양쪽에 넣어줘야지
# 내가 사용한 알고리즘은 프림알고리즘

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


# 다른 사람이 작성한 union find 사용해서 크루스칼로 최소스패닝트리 구한 방법

import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
 
Elist.sort(key=lambda x: x[2])
 
 
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)