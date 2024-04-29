def solution(n):
    dp = [0, 1, 2]
    for n in range(3, n+1):
        dp.append((dp[n-2] + dp[n-1]) % 1234567)
    return dp[n]