n, m = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

from collections import deque
q = deque([(0, 0, 1)])

visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True

result = 0
while q:
    y, x, level = q.popleft()
    if y == n-1 and x == m-1:
        result = level
        break
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= m or nx < 0 or board[ny][nx] == 0 or visited[ny][nx]:
            continue
        q.append((ny, nx, level + 1))
        visited[ny][nx] = True

print(result)