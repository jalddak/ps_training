import heapq
import sys
input = sys.stdin.readline

l = []
N = int(input())

result = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if len(l) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(l))
    else:
        heapq.heappush(l, n)

for r in result:
    print(r)