# 별로 차이없음

m, n = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque
q = deque()

board = []
total = 0
check = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == -1:
            continue
        if board[i][j] == 1:
            q.append((i, j))
        total += 1

result = 0
while q:
    y, x = q.popleft()
    result = board[y][x] - 1
    check += 1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] != 0:
            continue
        q.append((ny, nx))
        board[ny][nx] = board[y][x] + 1

if total != check:
    result = -1

print(result)