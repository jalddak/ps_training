import sys
def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())

board = [[False for _ in range(n)] for _ in range(n)]
switch = [[[] for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(m):
    x, y, a, b = map(lambda x:x-1, map(int, input().split()))
    switch[y][x].append((b, a))

board[0][0] = True
visited[0][0] = True

stack = [(0, 0)]
while stack:
    y, x = stack.pop()
    for sy, sx in switch[y][x]:
        if not board[sy][sx] and visited[sy][sx]:
            stack.append((sy, sx))
        board[sy][sx] = True
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= n or nx < 0 or visited[ny][nx]:
            continue
        if board[ny][nx]:
            stack.append((ny, nx))
        visited[ny][nx] = True

result = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            result += 1

print(result)