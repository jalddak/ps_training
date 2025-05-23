n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

minH = 101
maxH = 0
for i in range(n):
    maxH = max(maxH, max(board[i]))
    minH = min(minH, min(board[i]))

def dfs(h):
    visited = [[False for _ in range(n)] for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] <= h or visited[i][j]:
                continue
            visited[i][j] = True
            stack = [(i, j)]
            cnt += 1
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny >= n or ny < 0 or nx >= n or nx < 0 or board[ny][nx] <= h or visited[ny][nx]:
                        continue
                    visited[ny][nx] = True
                    stack.append((ny, nx))
                    
    return cnt

result = 1
for h in range(minH, maxH):
    temp = dfs(h)
    result = max(result, temp)

print(result)