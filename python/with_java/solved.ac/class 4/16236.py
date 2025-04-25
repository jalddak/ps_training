from collections import deque

n = int(input())

board = []
shark = []
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 0:
            continue
        if board[i][j] == 9:
            shark = [i, j, 2, 0]
            board[i][j] = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
while True:
    sy, sx, sSize, level = shark

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[sy][sx] = True
    q = deque([[sy, sx, 0]])

    candidates = []
    minTime = n * n

    while q:
        y, x, t = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            nt = t + 1
            if ny >= n or ny < 0 or nx >= n or nx < 0 or visited[ny][nx] or board[ny][nx] > sSize or nt > minTime:
                continue
            visited[ny][nx] = True

            if board[ny][nx] != 0 and board[ny][nx] < sSize:
                candidates.append((ny, nx))
                minTime = min(nt, minTime)
                continue

            q.append([ny, nx, nt])
    
    if not candidates:
        break
    answer += minTime
    candidates.sort(key=lambda x:(x[0], x[1]))

    ny, nx = candidates[0]
    if level + 1 == sSize:
        level = 0
        sSize += 1
    else:
        level += 1
    
    shark = [ny, nx, sSize, level]
    board[ny][nx] = 0

print(answer)