import sys
import heapq

input = sys.stdin.readline

n = int(input())
q = []
answer = []

for _ in range(n):
    c = int(input())
    if c == 0 and not q:
        answer.append(0)
    elif c == 0:
        answer.append(heapq.heappop(q))
    else:
        heapq.heappush(q, c)

for a in answer:
    print(a)
    