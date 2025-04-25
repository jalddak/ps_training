import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

target = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            target = [i, j]

answer = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

queue = deque([[target[0], target[1], 0]])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited[target[0]][target[1]] = True

while(queue):
    y, x, dtc = queue.popleft()
    answer[y][x] = dtc
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx] and board[ny][nx] == 1:
                queue.append([ny, nx, dtc+1])
                visited[ny][nx] = True

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if board[i][j] == 1:
                answer[i][j] = -1

for i in range(n):
    print(" ".join(map(str, answer[i])))