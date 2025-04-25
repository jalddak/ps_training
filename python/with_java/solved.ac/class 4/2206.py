n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
if n == 1 and m == 1:
    print(1)
    exit()

from collections import deque
queue = deque([[0, 0, 1, 0]])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0] = [True, True]

while queue:
    y, x, cnt, check = queue.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= m or nx < 0 or visited[ny][nx][check] or (check == 1 and board[ny][nx] == 1):
            continue
        nCheck = check
        if board[ny][nx] == 1:
            nCheck = 1
        if ny == n -1 and nx == m - 1:
            print(cnt + 1)
            exit()
        visited[ny][nx][nCheck] = True
        queue.append([ny, nx, cnt + 1, nCheck])

print(-1)