N = int(input())

nums = list(map(int, input().split()))

dp = {}
for i in range(N):
    if i == 0:
        dp[nums[i]] = 1
    else:
        max_cnt = 1
        for key in dp:
            if nums[i] > key:
                max_cnt = max(max_cnt, dp[key]+1)
        if nums[i] not in dp:
            dp[nums[i]] = max_cnt
        else:
            dp[nums[i]] = max(dp[nums[i]], max_cnt)

print(max(list(dp.values())))