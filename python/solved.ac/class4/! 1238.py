import sys
input = sys.stdin.readline

import heapq

N, M, X = map(int, input().split())
X -= 1

dist = [[0 for _ in range(N)] for _ in range(N)]
dist2 = [[0 for _ in range(N)] for _ in range(N)]
result = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    start, end, T = map(int, input().split())
    dist[start-1][end-1] = T
    dist2[end-1][start-1] = T

# for i in range(N):
#     print(dist2[i])
# print()

heap = []
for i in range(N):
    if dist[X][i] != 0:
        heapq.heappush(heap, (dist[X][i], i))
visited = [False for _ in range(N)]
visited[X] = True
while False in set(visited):
    distance, dest = heapq.heappop(heap)
    if not visited[dest]:
        result[X][dest] = distance
        visited[dest] = True
        for i in range(N):
            if dist[dest][i] != 0:
                heapq.heappush(heap, (distance + dist[dest][i], i))

heap = []
for i in range(N):
    if dist2[X][i] != 0:
        heapq.heappush(heap, (dist2[X][i], i))
visited = [False for _ in range(N)]
visited[X] = True
while False in set(visited):
    distance, dest = heapq.heappop(heap)
    if not visited[dest]:
        result[dest][X] = distance
        visited[dest] = True
        for i in range(N):
            if dist2[dest][i] != 0:
                heapq.heappush(heap, (distance + dist2[dest][i], i))


max_num = 0

for i in range(N):
    # print(result[i])
    max_num = max(max_num, result[i][X] + result[X][i])

print(max_num)