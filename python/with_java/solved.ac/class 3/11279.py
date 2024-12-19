import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
answer = []

for _ in range(n):
    num = int(input())
    if num == 0 and not q:
        answer.append(0)
    elif num == 0 and q:
        answer.append(-heapq.heappop(q))
    else:
        heapq.heappush(q, -num)

for a in answer:
    print(a)