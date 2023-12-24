import sys
input = sys.stdin.readline
N, K = map(int, input().split())

import heapq
js = []
for _ in range(N):
    heapq.heappush(js, tuple(map(int, input().split())))
bs = [int(input()) for _ in range(K)]
bs.sort()

candidate = []
result = 0
for b in bs:
    while len(js) != 0 and js[0][0] <= b:
        heapq.heappush(candidate, -heapq.heappop(js)[1])
    if candidate:
        result -= heapq.heappop(candidate)
print(result)