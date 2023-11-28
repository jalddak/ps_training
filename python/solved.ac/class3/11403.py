N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 or (board[i][r] == 1 and board[r][j] == 1):
                board[i][j] = 1

for i in range(N):
    print(" ".join(list(map(str, board[i]))))