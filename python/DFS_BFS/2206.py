# BFS
from collections import deque

N, M = list(map(int, input().split()))

board = [[int(s) for s in input()] for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# y, x, cnt, break
queue = deque([[0, 0, 1, 0]])
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

while len(queue) != 0:
    y, x, cnt, b = queue.popleft()
    if y == N-1 and x == M-1 and board[y][x] == 0:
        print(cnt)
        exit()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx][b] == 0:
            if b == 0 or board[ny][nx] == 0:
                nb = b
                if ny == N-1 and nx == M-1:
                    print(cnt+1)
                    exit()
                if board[ny][nx] == 1:
                    nb += 1
                visited[ny][nx][nb] = 1
                queue.append([ny, nx, cnt+1, nb])

print(-1)