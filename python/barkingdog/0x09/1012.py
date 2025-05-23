import sys
def input():
    return sys.stdin.readline().strip()

t = int(input())

answer = []
for _ in range(t):
    m, n, k = map(int, input().split())

    board = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or board[i][j] == 0:
                continue
            visited[i][j] = True
            cnt += 1
            stack = []
            stack.append((i, j))
            while stack:
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] == 0 or visited[ny][nx]:
                        continue
                    stack.append((ny, nx))
                    visited[ny][nx] = True

    answer.append(cnt)

print("\n".join(map(str, answer)))