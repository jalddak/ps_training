import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

from collections import deque

q = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                q.append([z, y, x, 0])

answer = 0

while(q):
    z, y, x, day = q.popleft()
    answer = day
    for d in range(6):
        nz = z + dz[d]
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = 1
            q.append([nz, ny, nx, day + 1])

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0:
                answer = -1
                break

print(answer)