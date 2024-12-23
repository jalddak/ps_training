n, m = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]

from collections import deque
q = deque([(0, 0, 1)])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[0][0] = True

while q:
    y, x, cnt = q.popleft()
    ncnt = cnt + 1
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx] == 1:
            if ny == n-1 and nx == m-1:
                print(ncnt)
                exit()
            visited[ny][nx] = True
            q.append((ny, nx, ncnt))
