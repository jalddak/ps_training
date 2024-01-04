T = int(input())

results = []
for _ in range(T):
    K = int(input())
    nums = list(map(int, input().split()))

    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    sums = [0]
    for i in range(K):
        sums.append(nums[i] + sums[i])

    for i in range(K,0,-1):
        for j in range(i, K+1):
            if i != j:
                dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
                dp[i][j] += sums[j]-sums[i-1]
    
    results.append(dp[1][K])

for r in results:
    print(r)