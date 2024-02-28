import sys
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())

board = []
for _ in range(R-1):
    board.append(list(input()[:-1]))
board.append(list(input()))
t_visited = [[False for _ in range(C)] for _ in range(R)]
r_visited = [[False for _ in range(C)] for _ in range(R)]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
t_loca = deque()
r_loca = deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'W':
            board[i][j] = '.'
            t_loca.append((i, j))
            t_visited[i][j] = True
        if board[i][j] == '*':
            r_loca.append((i, j))
            r_visited[i][j] = True

def move(loca, visited, entity):
    global board, dy, dx, R, C
    n_loca = deque()
    result = False
    while loca:
        y, x = loca.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == '.' and not visited[ny][nx]:
                n_loca.append((ny, nx))
                visited[ny][nx] = True
                board[ny][nx] = entity if entity == '*' else board[ny][nx]
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == 'H' and entity == 'T':
                result = True
    return n_loca, result

answer = 0
while t_loca:
    answer += 1
    r_loca, _ = move(r_loca, r_visited, '*')
    t_loca, result = move(t_loca, t_visited, 'T')
    if result:
        print(answer)
        exit()

print('FAIL')

    