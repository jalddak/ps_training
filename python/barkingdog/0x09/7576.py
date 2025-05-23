m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j, 0))

result = 0
while q:
    y, x, day = q.popleft()
    result = day
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] == -1 or board[ny][nx] == 1:
            continue
        q.append((ny, nx, day + 1))
        board[ny][nx] = 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result = -1

print(result)