import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

citys = [[] for _ in range(n)]

for _ in range(m):
    s, e, d = map(int, input().split())
    citys[s-1].append([e-1, d])

start, end = map(lambda x:x-1, map(int, input().split()))

import heapq
def dijkstra(start, end):
    global citys, n
    heap = [(0, start)]
    
    INF = int(1e9)
    distances = [[INF, []] for _ in range(n)]
    distances[start] = [0, []]
    while len(heap) != 0:
        dist, node = heapq.heappop(heap)
        if node == end:
            return dist, distances[node][1] + [node]
        if dist <= distances[node][0]:
            for c, d in citys[node]:
                if distances[c][0] > dist + d:
                    distances[c][0] = dist + d
                    distances[c][1] = distances[node][1] + [node]
                    heapq.heappush(heap, (dist + d, c))


dist, route = dijkstra(start, end)
print(dist)
print(len(route))
print(' '.join(map(str, map(lambda x:x+1, route))))