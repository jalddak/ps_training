# DFS

N, M = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
time = 0


while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    stack = []
    iceberg = []
    cnt = 0
    check = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                iceberg.append([i, j])
                visited[i][j] = True
                stack.append([i, j])
                cnt += 1
                if cnt >= 2:
                    print(time)
                    exit()
                while len(stack) != 0:
                    y, x = stack.pop()
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]
                        if 0 <= ny < N and 0 <= nx < M:
                            if board[ny][nx] > 0 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                stack.append([ny, nx])
                                iceberg.append([ny, nx])
                            elif board[ny][nx] == 0:
                                check[y][x] += 1
    time += 1
    if len(iceberg) == 0:
        print(0)
        exit()
    for y, x in iceberg:
        if board[y][x] > 0:
            board[y][x] -= check[y][x]
            if board[y][x] < 0:
                board[y][x] = 0