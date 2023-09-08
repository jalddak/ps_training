# BFS
# pypy3 에서만 통과, python3 에서는 통과못함

from collections import deque

r, c = list(map(int, input().split()))

board = []
for _ in range(r):
    row = list(input())
    board.append(row)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 05

for i in range(r):
    for j in range(c):
        visited = [[False for _ in range(c)] for _ in range(r)]
        if board[i][j] == 'L' and not visited[i][j]:
            visited[i][j] = True
            queue = deque([[i, j, 0]])
            while len(queue) != 0:
                y, x, t = queue.popleft()
                if t > answer:
                    answer = t
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == 'L' and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append([ny, nx, t+1])

print(answer)