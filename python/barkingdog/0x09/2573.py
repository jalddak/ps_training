n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = 0
while True:
    cnt = 0
    result += 1
    for i in range(n):
        for j in range(m):
            if board[i][j] <= 0 or visited[i][j] == result:
                continue
            cnt += 1
            if cnt == 2:
                print(result - 1)
                exit()
            visited[i][j] = result
            stack = [(i, j)]
            nBoard = [board[i][:] for i in range(n)]
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny >= n or ny < 0 or nx >= m or nx < 0:
                        continue
                    if board[ny][nx] <= 0:
                        nBoard[y][x] -= 1
                        continue
                    if visited[ny][nx] == result:
                        continue
                    visited[ny][nx] = result
                    stack.append((ny, nx))
            board = nBoard
    if cnt == 0:
        print(0)
        exit()