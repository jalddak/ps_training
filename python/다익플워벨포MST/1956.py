import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = int(1e9)

board = [[INF for _ in range(V)] for _ in range(V)]
for _ in range(E):
    s, e, c = map(int, input().split())
    board[s-1][e-1] = c

for m in range(V):
    for i in range(V):
        for j in range(V):
            board[i][j] = min(board[i][j], board[i][m] + board[m][j])

result = INF
for i in range(V):
    result = min(result, board[i][i])

print(-1) if result == INF else print(result)