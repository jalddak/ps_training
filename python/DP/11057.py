N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)]

dp[0] = [1] * 10

for i in range(1, N):
    before_sum = sum(dp[i-1])
    for j in range(10):
        if j > 0:
            before_sum -= dp[i-1][j-1]
        dp[i][j] = before_sum

print(sum(dp[-1])%10007)