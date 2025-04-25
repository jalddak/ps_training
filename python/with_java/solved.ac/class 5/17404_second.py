n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
inf = 1000 * 1000 + 1

candidates = []

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        result = costs[0][i] + costs[-1][j]
        dp = costs[1][:]
        dp[i] = inf

        for k in range(2, n-1):
            r, g, b = costs[k]
            dp = [r + min(dp[1:]), g + min(dp[0], dp[2]), b + min(dp[:-1])]
        
        dp[j] = inf
        result += min(dp)
        candidates.append(result)

print(min(candidates))