# BFS
from collections import deque

M, N, K = list(map(int, input().split()))

board = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    fx, fy, sx, sy = list(map(int, input().split()))
    for i in range(fy, sy):
        for j in range(fx, sx):
            board[i][j] = 1


visited = [[False for _ in range(N)] for _ in range(M)]
result = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            queue = deque([[i, j]])
            area = 0
            while len(queue) != 0:
                area += 1
                y, x = queue.popleft()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] == 0:
                        visited[ny][nx] = True
                        queue.append([ny, nx])
            result.append(area)

result.sort()
print(len(result))
for num in result:
    print(num, end=' ')