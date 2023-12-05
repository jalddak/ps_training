import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)

board = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    board[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    board[a-1][b-1] = min(board[a-1][b-1], c)

for r in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][r] + board[r][j])

for i in range(n):
    for j in range(n):
        if board[i][j] == INF:
            print(0, end=' ')
        else:
            print(board[i][j], end=' ')
    print()