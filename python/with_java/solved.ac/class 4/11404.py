import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 100000 * 100 * 100 + 1

board = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    board[i][i] = 0

for _ in range(m):
    s, e, cost = map(int, input().split())
    s -= 1
    e -= 1
    board[s][e] = min(board[s][e], cost)

for k in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])


for i in range(n):
    for j in range(n):
        if board[i][j] == INF:
            board[i][j] = 0
    print(" ".join(map(str, board[i])))