import sys
input = sys.stdin.readline

N = int(input())

times = [0 for _ in range(N)]
# parent cnt array
pca = [0 for _ in range(N)]
childs = [[] for _ in range(N)]
for i in range(N):
    param = list(map(int, input().split()))
    times[i] = param[0]
    pca[i] = len(param)-2
    for j in range(1, len(param)-1):
        childs[param[j]-1].append(i)

import heapq
heap = []
for i in range(N):
    if pca[i] == 0:
        heapq.heappush(heap, (times[i], i))

results = [0 for _ in range(N)]
while heap:
    time, n = heapq.heappop(heap)
    results[n] = time
    for child in childs[n]:
        pca[child] -= 1
        if pca[child] == 0:
            heapq.heappush(heap, (times[child] + time, child))

for t in results:
    print(t)