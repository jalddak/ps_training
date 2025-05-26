from collections import deque

n, m, k = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

visited[0][0] = k
q = deque([(k, 0, 0, 1)])

dy = [-1, 0, 1, 0]
dx = [0 ,1, 0, -1]

result = -1
while q:
    cnt, y, x, depth = q.popleft()
    if y == n - 1 and x == m - 1:
        result = depth
        break
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= m or nx < 0 or (board[ny][nx] == 1 and cnt == 0):
            continue
        ncnt = cnt
        if board[ny][nx] == 1:
            ncnt = cnt - 1
        if visited[ny][nx] >= ncnt:
            continue
        visited[ny][nx] = ncnt
        q.append((ncnt, ny, nx, depth + 1))
        if ny == n - 1 and nx == m - 1:
            result = depth + 1
            print(result)
            exit()

print(result)