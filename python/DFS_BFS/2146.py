from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

num = 2
wss = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            board[i][j] = num
            visited[i][j] = 1
            stack = [[i, j]]
            water_stack = deque([num])
            while len(stack) != 0:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0:
                        if board[ny][nx] == 1:
                            board[ny][nx] = num
                            visited[ny][nx] = 1
                            stack.append([ny, nx])
                        elif board[ny][nx] == 0:
                            water_stack.append([ny, nx, 1])
            num += 1
            wss.append(water_stack)
            
result = -1
for water_stack in wss:
    num = water_stack.popleft()
    check = 0
    while len(water_stack) != 0:
        y, x, cnt = water_stack.popleft()
        if result != -1 and result <= cnt:
            break
        visited[y][x] = 1
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] != 1:
                    water_stack.append([ny, nx, cnt+1])
                    visited[ny][nx] = 1
                if board[ny][nx] != num:
                    if board[ny][nx] > 0:
                        if result == -1 or result > cnt:
                            result = cnt
                            check = 1
                            break
        if check == 1:
            break

print(result)