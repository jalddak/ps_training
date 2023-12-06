n, m, r = map(int, input().split())

items = list(map(int, input().split()))

INF = int(1e9)

board = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    board[i][i] = 0

for _ in range(r):
    a, b, distance = map(int, input().split())
    board[a-1][b-1] = distance
    board[b-1][a-1] = distance

for mid in range(n):
    for i in range(n):
        for j in range(n):
            board[i][j] = min(board[i][j], board[i][mid] + board[mid][j])

result = 0
for dists in board:
    temp = 0
    for i in range(len(dists)):
        if dists[i] <= m:
            temp += items[i]
    result = max(result, temp)

print(result)