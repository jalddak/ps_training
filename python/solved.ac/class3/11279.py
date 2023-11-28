import sys
input = sys.stdin.readline

import heapq

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-x, x))