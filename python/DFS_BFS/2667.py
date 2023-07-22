# bfs or dfs

# bfs
from collections import deque

N = int(input())

board = []
for _ in range(N):
    string = input()
    row = []
    for char in string:
        row.append(char)
    row = list(map(int, row))
    board.append(row)

visited = [[False for _ in range(N)] for _ in range(N)]

queue = deque([])
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

group_num = 0
homes = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0 and not visited[i][j]:
            visited[i][j] = True
            queue.append([i, j])
            group_num += 1
            home_num = 0
            while len(queue) != 0:
                home_num += 1
                y, x = queue.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] != 0:
                        queue.append([ny, nx])
                        visited[ny][nx] = True
            homes.append(home_num)
        elif board[i][j] == 0:
            visited[i][j] = True

print(group_num)
homes.sort()
for i in range(group_num):
    print(homes[i])