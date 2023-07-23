# bfs

from collections import deque

M, N = list(map(int, input().split()))

board = []
loca = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            loca.append([i, j])
    board.append(row)

queue = deque([loca])
day = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while len(queue) != 0:
    loca = deque(queue.popleft())
    new = []
    while len(loca) != 0:
        y, x = loca.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
                new.append([ny, nx])
                board[ny][nx] = 1
    if len(new) != 0:
        queue.append(new)
        day += 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            exit()

print(day)