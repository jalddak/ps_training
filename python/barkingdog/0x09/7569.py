import sys
def input():
    return sys.stdin.readline().strip()

m, n, h = map(int, input().split())

from collections import deque
q = deque()

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

total = 0
box = []
for i in range(h):
    box.append([])
    for j in range(n):
        box[i].append(list(map(int, input().split())))
        for k in range(m):
            if box[i][j][k] == -1:
                continue
            total += 1
            if box[i][j][k] == 1:
                q.append((i, j, k, 0))

result = 0
check = 0
while q:
    z, y, x, day = q.popleft()
    check += 1
    result = day
    for d in range(6):
        nz = z + dz[d]
        ny = y + dy[d]
        nx = x + dx[d]
        if nz >= h or nz < 0 or ny >= n or ny < 0 or nx >= m or nx < 0 or box[nz][ny][nx] != 0:
            continue
        box[nz][ny][nx] = 1
        q.append((nz, ny, nx, day + 1))

if total != check:
    result = -1

print(result)
