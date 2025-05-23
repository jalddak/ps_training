n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
area = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 or visited[i][j]:
            continue
        visited[i][j] = True
        cnt += 1
        stack = [(i, j)]

        temp = 0
        while stack:
            y, x = stack.pop()
            temp += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] == 0 or visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                stack.append((ny, nx))
        area = max(area, temp)

print(cnt)
print(area)