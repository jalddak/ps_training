N = int(input())
A = list(map(int, input().split()))

dp = {}

for i in range(N):
    cnt = 1
    for key in dp:
        if A[i] < key:
            cnt = max(cnt, dp[key]+1)
    if A[i] not in dp:
        dp[A[i]] = cnt
    else:
        dp[A[i]] = max(cnt, dp[A[i]])
    
max_cnt = max(list(dp.values()))
print(max_cnt)