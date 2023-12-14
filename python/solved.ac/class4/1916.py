import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

citys = [[] for _ in range(N)]

for _ in range(M):
    s, e, d = map(int, input().split())
    citys[s-1].append([e-1, d])

import heapq
def dijkstra(start, end):
    heap = [(0, start)]
    INF = int(1e9)
    checked = [INF for _ in range(N)]
    checked[start] = 0

    while len(heap) != 0:
        dist, city = heapq.heappop(heap)
        if city == end:
            return checked[city]
        if dist > checked[city]:
            continue
        for next, plus in citys[city]:
            n_dist = dist + plus
            if checked[next] > n_dist:
                checked[next] = n_dist
                heapq.heappush(heap, (n_dist, next))

start, end = map(int, input().split())
print(dijkstra(start-1, end-1))