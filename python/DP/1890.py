import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if i == N-1 and j == N-1:
            dp[i][j] = 1
            continue
        dmove = i + board[i][j]
        rmove = j + board[i][j]
        if 0 <= dmove < N:
            dp[i][j] += dp[dmove][j]
        if 0 <= rmove < N:
            dp[i][j] += dp[i][rmove]

print(dp[0][0])