import sys
input = sys.stdin.readline

N = int(input())

xlist, ylist,zlist = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    xlist.append([x, i])
    ylist.append([y, i])
    zlist.append([z, i])

xlist.sort(key=lambda x:x[0])
ylist.sort(key=lambda x:x[0])
zlist.sort(key=lambda x:x[0])

def addEdge(edges, l):
    for i in range(N-1):
        loca, node = l[i]
        n_loca, n_node = l[i+1]
        edges[node] = edges.get(node, {})
        edges[n_node] = edges.get(n_node, {})
        cost = abs(loca-n_loca)
        edges[node][n_node] = min(edges[node].get(n_node, cost), cost)
        edges[n_node][node] = min(edges[n_node].get(node, cost), cost)

edges = {}
addEdge(edges, xlist)
addEdge(edges, ylist)
addEdge(edges, zlist)

visited = [False for _ in range(N)]

import heapq
heap = [(0, 0)]

result = 0
while heap:
    cost, node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    result += cost
    for next in edges[node]:
        n_cost = edges[node][next]
        if visited[next]:
            continue
        heapq.heappush(heap, (n_cost, next))

print(result)
