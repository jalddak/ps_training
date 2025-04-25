import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = 1 if board[i][k] == 1 and board[k][j] == 1 else board[i][j]
for i in range(n):
    print(" ".join(map(str, board[i])))