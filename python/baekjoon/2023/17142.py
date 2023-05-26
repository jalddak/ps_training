from itertools import combinations
from collections import deque

n, m = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

virus = []
free = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append([i, j, 0])
            board[i][j] = '*'
        elif board[i][j] == 0:
            free += 1
            board[i][j] = 'F'
        else:
            board[i][j] = '-'

actives = list(combinations(virus, m))

least = n*n

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
check = 0

for active in actives:
    filled = 0
    active = deque(active)
    time = 0
    copy = []
    for i in range(n):
        copy.append(board[i][:])
    while len(active) != 0 and free != filled and time < least:
        y, x, t = active.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n and copy[ny][nx] != '-':
                if copy[ny][nx] == 'F':
                    time = t + 1
                    copy[ny][nx] = time
                    active.append([ny, nx, time])
                    filled += 1
                elif copy[ny][nx] == '*':
                    time = t + 1
                    copy[ny][nx] = time
                    active.append([ny, nx, time])
    
    if free == filled:
        check = 1
        least = min(least, time)

if check == 0:
    least = -1

print(least)