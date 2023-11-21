import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = [[-1 for _ in range(m)] for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            queue.append([i, j])
            result[i][j] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while len(queue) != 0:
    y, x = queue.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < m and result[ny][nx] == -1 and board[ny][nx] != 0:
                result[ny][nx] = result[y][x] + 1
                queue.append([ny, nx])

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            result[i][j] = 0


for i in range(n):
    for j in range(m):
        print(result[i][j], end = " ")
    print()

