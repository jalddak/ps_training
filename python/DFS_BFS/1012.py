# BFS or DFS
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

T = int(input())

for _ in range(T):
    M, N, K = list(map(int, input().split()))
    board = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        X, Y = list(map(int, input().split()))
        board[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                visited[i][j] = True
                if board[i][j] == 1:
                    cnt += 1
                    queue = deque([[i, j]])
                    while len(queue) != 0:
                        y, x = queue.popleft()
                        for d in range(4):
                            ny = y + dy[d]
                            nx = x + dx[d]
                            if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and not visited[ny][nx]:
                                queue.append([ny, nx])
                                visited[ny][nx] = True
    print(cnt)
