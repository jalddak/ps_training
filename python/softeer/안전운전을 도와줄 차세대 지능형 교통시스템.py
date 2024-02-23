import sys

N, T = map(int, input().split())
signs = []
for i in range(4):
    board = [[False for _ in range(4)] for _ in range(4)]
    for j in range(4):
        if i == j:
            continue
        board[i][j] = True
    signs.append(board)
for i in range(4):
    board = [[False for _ in range(4)] for _ in range(4)]
    for j in range(4):
        if i == j or i + 1 == j or (i == 3 and j == 0):
            continue
        board[i][j] = True
    signs.append(board)
for i in range(4):
    board = [[False for _ in range(4)] for _ in range(4)]
    for j in range(4):
        if i == j or i - 1 == j or (i == 0 and j == 3):
            continue
        board[i][j] = True
    signs.append(board)

        
sign_infos = [[list(map(lambda x:x-1, map(int, input().split()))) for _ in range(N)] for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

visited = {(0, 0)}
def recursion(depth, y, x, entrace):
    global sign_infos, signs, N, T
    if depth == T:
        return
    sign_info = sign_infos[y][x][depth % 4]
    sign = signs[sign_info][entrace]
    for d in range(4):
        if not sign[d]:
            continue
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        next_entrace = d+2 if d+2 < 4 else d+2-4
        visited.add((ny, nx))
        recursion(depth+1, ny, nx, next_entrace)

recursion(0, 0, 0, 1)
print(len(visited))