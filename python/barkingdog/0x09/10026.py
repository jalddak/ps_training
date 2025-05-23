n = int(input())
board = [list(input()) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

rg = set(["R", "G"])

def dfs(check):
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True
            result += 1
            stack = [(i, j)]
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny >= n or ny < 0 or nx >= n or nx < 0 or visited[ny][nx]:
                        continue
                    if not check and board[ny][nx] != board[y][x]:
                        continue
                    if check and ((board[y][x] in rg and board[ny][nx] == "B") or (board[y][x] == "B" and board[ny][nx] in rg)):
                        continue
                    stack.append((ny, nx))
                    visited[ny][nx] = True
    return result

answer = []
answer.append(dfs(False))
answer.append(dfs(True))

print(" ".join(map(str, answer)))
