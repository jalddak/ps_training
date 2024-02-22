import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def calc_outer(board, y, x):
    global N, M

    board[y][x] = -1
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<N and 0<=nx<M and board[ny][nx] == 0:
                board[ny][nx] = -1
                stack.append((ny, nx))

calc_outer(board, 0, 0)
time = 0
while True:
    nd = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt = 0
                for d in range(4):
                    ay = i + dy[d]
                    ax = j + dx[d]
                    if 0<=ay<N and 0<=ax<M and board[ay][ax] == -1:
                        cnt += 1
                if cnt >= 2:
                    nd.append((i, j))
    if not nd:
        break
    time += 1
    for y, x in nd:
        calc_outer(board, y, x)

print(time)
            