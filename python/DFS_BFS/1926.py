# DFS

n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
result = [0, 0]

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == 1:
            stack = [[i, j]]
            visited[i][j] = 1
            result[0] += 1
            size = 0
            while len(stack) != 0:
                size += 1
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and board[ny][nx] == 1:
                        stack.append([ny, nx])
                        visited[ny][nx] = 1
            result[1] = max(result[1], size)

for r in result:
    print(r)