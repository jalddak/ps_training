import sys
input = sys.stdin.readline

n = int(input())

courses = [list(map(int, input().split())) for _ in range(n)]
courses.sort(key=lambda x:(x[1], x[0]))

cnt = 0
time = 0
for i in range(n):
    if courses[i][0] >= time:
        cnt += 1
        time = courses[i][1]

print(cnt)

import sys
input = sys.stdin.readline

n = int(input())

import heapq

heap = []
for _ in range(n):
    s, f = map(int, input().split())
    heapq.heappush(heap, (f, s))

cnt = 0
time = 0
while heap:
    f, s = heapq.heappop(heap)
    if s >= time:
        cnt += 1
        time = f

print(cnt)