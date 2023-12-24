import sys
input = sys.stdin.readline

N, M = map(int, input().split())

infos = [[0, []] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x:x-1, map(int, input().split()))
    infos[A][1].append(B)
    infos[B][0] += 1

import heapq
heap = []
for i in range(N):
    if infos[i][0] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    n = heapq.heappop(heap)
    result.append(n)
    for child in infos[n][1]:
        infos[child][0] -= 1
        if infos[child][0] == 0:
            heapq.heappush(heap, child)

print(" ".join(list(map(str, (map(lambda x:x+1, result))))))