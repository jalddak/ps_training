# BFS

from collections import deque

R, C = list(map(int, input().split()))
board = []
S = []
water = []
for i in range(R):
    board.append(list(input()))
    for j in range(C):
        if board[i][j] == 'S':
            S = [i, j]
        elif board[i][j] == '*':
            water.append([i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited = [[False for _ in range(C)] for _ in range(R)]
visited[S[0]][S[1]] = True
board[S[0]][S[1]] = '.'

queue = deque([[S[0], S[1], 0]])

while len(queue) != 0:
    next = []
    for wy, wx in water:
        for d in range(4):
            nwy = wy + dy[d]
            nwx = wx + dx[d]
            if 0 <= nwy < R and 0 <= nwx < C and board[nwy][nwx] == '.':
                board[nwy][nwx] = '*'
                next.append([nwy, nwx])
    water = next

    n_queue = deque([])
    while len(queue) != 0:
        y, x, cnt = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                if board[ny][nx] == '.':
                    visited[ny][nx] = True
                    n_queue.append([ny, nx, cnt+1])
                elif board[ny][nx] == 'D':
                    print(cnt + 1)
                    exit(0)
    queue = n_queue

print('KAKTUS')