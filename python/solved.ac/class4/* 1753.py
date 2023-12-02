import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input()) - 1
INF = int(1e9)
l = [[] for _ in range(V)]
for _ in range(E):
    start, end, dist = map(int, input().split())
    l[start-1].append([end-1, dist])

import heapq

heap = [(0, K)]

result = [INF for _ in range(V)]
result[K] = 0
while len(heap) != 0:
    dist, dest = heapq.heappop(heap)
    if result[dest] == dist:
        for n, d in l[dest]:
            length = dist + d
            if result[n] > length:
                result[n] = length
                heapq.heappush(heap, (length, n))


for r in result:
    if r == INF:
        print("INF")
    else:
        print(r)

# 시간 초과 (해결)
# 10퍼센트 틀림 : 문제 제대로 안읽음
# dict 로 안되는 이유 : 문제에서 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다. 라고 말함.
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input()) - 1
INF = int(1e9)
d = {}
for _ in range(E):
    start, end, dist = map(int, input().split())
    if start-1 not in d:
        d[start-1] = {end-1:dist}
    else:
        d[start-1][end-1] = dist

import heapq

heap = [(0, K)]

result = [INF for _ in range(V)]
result[K] = 0
# while len(heap) != 0 and INF in set(result): result 체크 과정에서 시간초과남
while len(heap) != 0:
    dist, dest = heapq.heappop(heap)
    if result[dest] == dist:
        if dest in d:
            for n in d[dest]:
                length = dist + d[dest][n]
                if result[n] > length:
                    result[n] = length
                    heapq.heappush(heap, (length, n))


for r in result:
    if r == INF:
        print("INF")
    else:
        print(r)

# 메모리초과
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input()) - 1
INF = int(1e9)
board = [[INF for _ in range(V)] for _ in range(V)]

import heapq

for _ in range(E):
    start, end, dist = map(int, input().split())
    board[start-1][end-1] = dist

heap = [(0, K)]

result = [INF for _ in range(V)]
while len(heap) != 0 and INF in set(result):
    dist, dest = heapq.heappop(heap)
    if result[dest] >= dist:
        result[dest] = dist
        for i in range(V):
            length = dist + board[dest][i]
            if result[i] > length:
                result[i] = length
                heapq.heappush(heap, (length, i))


for r in result:
    if r == INF:
        print("INF")
    else:
        print(r)