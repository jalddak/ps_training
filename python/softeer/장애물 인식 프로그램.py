import sys

n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = []
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        visited[i][j] = True
        if board[i][j] == 0:
            continue
        stack = [[i, j]]
        cnt = 0
        while stack:
            y, x = stack.pop()
            cnt += 1
            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]
                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and board[ny][nx] == 1:
                    visited[ny][nx] = True
                    stack.append([ny, nx])
        result.append(cnt)

print(len(result))
result.sort()
for n in result:
    print(n)