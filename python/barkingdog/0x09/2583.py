n, m, k = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for i in range(sy, ey):
        for j in range(sx, ex):
            board[i][j] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
areas = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] or board[i][j] == 1:
            continue
        visited[i][j] = True
        stack = [(i, j)]
        cnt += 1
        area = 0

        while stack:
            y, x = stack.pop()
            area += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] == 1 or visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                stack.append((ny, nx))
        areas.append(area)

print(cnt)
areas.sort()
print(" ".join(map(str, areas)))