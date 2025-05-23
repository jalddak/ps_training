from collections import deque
import sys
def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]

if n == 1 and m == 1:
    print(1)
    exit()

INF = n * m + 1
visited = [[[INF for _ in range(2)] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque([(0, 0, 0)])

flag = False
while q:
    y, x, p = q.popleft()
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny >= n or ny < 0 or nx >= m or nx < 0 or (board[ny][nx] == 1 and p == 1) or (visited[ny][nx][p] <= visited[y][x][p] + 1):
            continue
        np = p
        if board[ny][nx] == 1:
            np = 1 
        if ny == n-1 and nx == m-1:
            print(visited[y][x][p] + 1)
            exit()
        visited[ny][nx][np] = visited[y][x][p] + 1
        q.append((ny, nx, np))

print(-1)