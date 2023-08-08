N = int(input())

price = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]

for i in range(N):
    candidate = [price[i]]
    n = (i+1) // 2
    for j in range(1, n+1):
        candidate.append(dp[j]+dp[i+1-j])
    dp[i+1] = max(candidate)

print(dp[-1])