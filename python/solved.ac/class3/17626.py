N = int(input())

dp = [0 for _ in range(N+1)]
nums = []
for n in range(1, N+1):
    if n ** 0.5 == int(n**0.5):
        dp[n] = 1
        nums.append(n)
    elif dp[n] == 0:
        dp[n] = dp[n-1] + 1
        for num in nums:
            dp[n] = min(dp[n-num] + 1, dp[n])

print(dp[N])