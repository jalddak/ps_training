import sys
input = sys.stdin.readline

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque

q = deque()

for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            q.append([y, x, 0])

answer = 0

while(q):
    y, x, day = q.popleft()
    answer = day
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < m and box[ny][nx] == 0:
            box[ny][nx] = 1
            q.append([ny, nx, day + 1])

for y in range(n):
    for x in range(m):
        if box[y][x] == 0:
            answer = -1
            break

print(answer)