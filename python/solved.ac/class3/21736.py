N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "I":
            stack = [(i, j)]
            visited[i][j] = True
            while len(stack) != 0:
                y, x = stack.pop()
                if board[y][x] == "P":
                    result += 1
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] != "X" and not visited[ny][nx]:
                        stack.append((ny, nx))
                        visited[ny][nx] = True
            break

print(result)


