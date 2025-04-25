import sys
input = sys.stdin.readline

n = int(input())
board = [list(input()[:-1]) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
normal = 0
strange = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal += 1
            visited[i][j] = True
            stack = [(i, j)]
            while(stack):
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and board[y][x] == board[ny][nx]:
                        visited[ny][nx] = True
                        stack.append((ny, nx))

visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            strange += 1
            visited[i][j] = True
            stack = [(i, j)]
            while(stack):
                y, x = stack.pop()
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and (board[y][x] == board[ny][nx] or (board[y][x] in ['R', 'G'] and board[ny][nx] in ['R', 'G'])):
                        visited[ny][nx] = True
                        stack.append((ny, nx))
    
print(normal, strange)