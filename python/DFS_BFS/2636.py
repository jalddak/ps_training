# BFS

from collections import deque

r, c = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(r)]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
queue = deque([[0, 0]])
board[0][0] = 2

def air_check(queue):
    global r, c, dy, dx, board

    nqueue = deque([])
    while len(queue) != 0:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] != 2:
                if board[ny][nx] == 0:
                    board[ny][nx] = 2
                    queue.append([ny, nx])
                elif board[ny][nx] == 1:
                    board[ny][nx] = 2
                    nqueue.append([ny, nx])

    return nqueue

time = 0
last = 0
while True:
    queue = air_check(queue)
    if len(queue) == 0:
        print(time)
        print(last)
        break
    else:
        time += 1
        last = len(queue)