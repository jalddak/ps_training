tcCnt = int(input())

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

answer = []

def dfs(y, x, k, n, d, board):
    if y >= n or y < 0 or x >= n or x < 0 or board[y][x] == 0:
        return False
    if board[y][x] == k:
        return True
    
    result = dfs(y + dy[d], x + dx[d], k, n, d, board)
    if result:
        board[y][x] = k
    return result

for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    half = n // 2
    board[half-1][half-1] = 2
    board[half-1][half] = 1
    board[half][half-1] = 1
    board[half][half] = 2

    for _ in range(m):
        x, y, k = map(int, input().split())
        x -= 1
        y -= 1

        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            dfs(ny, nx, k, n, d, board)
        board[y][x] = k
    
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                black += 1
            if board[i][j] == 2:
                white += 1
    
    sb += str(black) + " " + str(white)
    answer.append(sb)
        
for a in answer:
    print(a)