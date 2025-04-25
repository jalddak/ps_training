import sys
input = sys.stdin.readline

import heapq

n = int(input())

heap = []
answers = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if heap:
            absNum, realNum = heapq.heappop(heap)
        else:
            realNum = 0
        answers.append(realNum)
    else:
        heapq.heappush(heap, (abs(num), num))

for a in answers:
    print(a)