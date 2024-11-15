import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for y in range(n):
        for x in range(m):
            if visited[y][x]:
                continue
            visited[y][x] = True
            if board[y][x] == 0:
                continue
            cnt += 1
            stack = [(y, x)]
            while stack:
                cy, cx = stack.pop()
                for d in range(4):
                    ny = cy + dy[d]
                    nx = cx + dx[d]
                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if visited[ny][nx]:
                        continue
                    elif board[ny][nx] == 1:
                        visited[ny][nx] = True
                        stack.append((ny, nx))
    
    print(cnt)

