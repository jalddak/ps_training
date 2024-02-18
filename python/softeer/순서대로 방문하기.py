import sys
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

v = deque([tuple(map(lambda x:x-1, map(int, input().split()))) for _ in range(m)])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def copy_board(board):
    copy = []
    for row in board:
        copy.append(row[:])
    return copy

queue = deque([[v[0], 1, copy_board(board)]])

result = 0
while queue:
    loca, index, board = queue.popleft()
    if index == m:
        result += 1
        continue
    y, x = loca
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0<=ny<n and 0<=nx<n and board[ny][nx] == 0:
            if v[index] == (ny, nx):
                copy = copy_board(board)
                copy[ny][nx] = 1
                queue.append([(ny, nx), index + 1, copy])
            elif (ny, nx) in v:
                continue
            else:
                copy = copy_board(board)
                copy[ny][nx] = 1
                queue.append([(ny, nx), index, copy])
                
print(result)