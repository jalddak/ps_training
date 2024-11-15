n = int(input())

dp = [0 for _ in range(n+1)]
nums = []

for a in range(1, n+1):
    if a ** 0.5 == int(a ** 0.5):
        nums.append(a)
        dp[a] = 1
    else:
        dp[a] = dp[a-1] + 1
        for num in nums:
            dp[a] = min(dp[a], dp[a-num] + 1)

print(dp[n])
