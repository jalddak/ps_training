import sys
input = sys.stdin.readline

N = int(input())
childs = [[] for _ in range(N)]
pcnts = [0 for _ in range(N)]
times = [0 for _ in range(N)]

for i in range(N):
    info = list(map(int, input().split()))
    time = info[0]
    times[i] = time

    pcnt = info[1]
    pcnts[i] = pcnt
    if pcnt == 0:
        continue
    
    for p in info[2:]:
        p -= 1
        childs[p].append(i)

import heapq
heap = []
for i in range(N):
    if pcnts[i] == 0:
        heapq.heappush(heap, (times[i], i))

result = 0
while heap:
    time, node = heapq.heappop(heap)
    result = time
    for c in childs[node]:
        pcnts[c] -= 1
        if pcnts[c] == 0:
            heapq.heappush(heap, (times[c] + time, c))

print(result)