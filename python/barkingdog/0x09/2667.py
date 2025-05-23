n = int(input())

board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

cnt = 0
areas = []
for i in range(n):
    for j in range(n):
        if visited[i][j] or board[i][j] == 0:
            continue
        visited[i][j] = True
        cnt += 1
        area = 0
        stack = [(i, j)]
        while stack:
            y, x = stack.pop()
            area += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if ny >= n or ny < 0 or nx >= n or nx < 0 or board[ny][nx] == 0 or visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                stack.append((ny, nx))
        areas.append(area)

print(cnt)
areas.sort()
print("\n".join(map(str, areas)))