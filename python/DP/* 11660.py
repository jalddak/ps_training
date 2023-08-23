import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]
s_board = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        s_board[i][j] = board[i][j]
        if j > 0:
            s_board[i][j] += s_board[i][j-1]
    for j in range(N):
        if i > 0:
            s_board[i][j] += s_board[i-1][j]

for _ in range(M):
    y1, x1, y2, x2 = list(map(lambda x:x-1, list(map(int, input().split()))))
    result = s_board[y2][x2]
    if y1 > 0:
        result -= s_board[y1-1][x2]
    if x1 > 0:
        result -= s_board[y2][x1-1]
    if y1 > 0 and x1 > 0:
        result += s_board[y1-1][x1-1]
    print(result)
    

