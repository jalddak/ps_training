# DFS

# 36퍼 쯤에서 recursionerror가 나와서 리미트 해제해줌
# 깊이를 너무 깊게 가능하게 하면 pypy3 에서 메모리 초과가 남.
import sys
sys.setrecursionlimit(10 ** 4)

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    global dy, dx, board, visited, n
    candidate = []
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > board[y][x]:
            if visited[ny][nx] == 0:
                candidate.append(dfs(ny, nx))
            else:
                candidate.append(visited[ny][nx])
    visited[y][x] = 1
    if len(candidate) != 0:
        visited[y][x] += max(candidate)
    return visited[y][x]
                

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j)

result = 0
for i in range(n):
    result = max(result, max(visited[i]))

print(result)