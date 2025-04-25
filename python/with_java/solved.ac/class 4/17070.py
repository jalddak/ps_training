n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    if board[0][i] == 1:
        break
    dp[0][i] = [1, 0, 0]

for i in range(1, n):
    for j in range(2, n):
        if board[i][j] == 1:
            continue
        n1 = dp[i][j-1][0] + dp[i][j-1][2]
        n2 = dp[i-1][j][1] + dp[i-1][j][2]
        n3 = 0 if board[i][j-1] == 1 or board[i-1][j] == 1 else sum(dp[i-1][j-1])
        dp[i][j] = [n1, n2, n3]

print(sum(dp[n-1][n-1]))