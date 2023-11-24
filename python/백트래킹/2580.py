board = [list(map(int, input().split())) for _ in range(9)]

check_c = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            check_c.append([i, j])

def check(y, x, n):
    sy, sx = (0, 0)

    if 3 <= y < 6:
        sy = 3
    elif y >= 6:
        sy = 6
    if 3 <= x < 6:
        sx = 3
    elif x >= 6:
        sx = 6
    
    for j in range(9):
        if board[y][j] == n:
            return False
    
    for i in range(9):
        if board[i][x] == n:
            return False
    
    for i in range(sy, sy+3):
        for j in range(sx, sx+3):
            if board[i][j] == n:
                return False

    return True

def dfs(index):
    global check_c
    if index == len(check_c):
        for i in range(9):
            print(board[i][0],board[i][1],board[i][2],board[i][3],board[i][4],board[i][5],board[i][6],board[i][7],board[i][8])
        exit()
    y, x = check_c[index]
    for n in range(1, 10):
        if check(y, x, n):
            board[y][x] = n
            if not dfs(index+1):
                continue
    board[y][x] = 0
    return False
        

dfs(0)