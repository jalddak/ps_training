N = int(input())

sq = list(map(int, input().split()))

def ascend(sq):
    global N
    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if sq[i] > sq[j]:
                dp[i] = max(dp[i], dp[j]+1)
    for i in range(1,N):
        dp[i] = max(dp[i], dp[i-1])
    return dp

dp = ascend(sq)
rdp = ascend(list(reversed(sq)))
rdp.reverse()
print(dp, rdp)
result = max(max(dp), max(rdp))
for i in range(N):
    result = max(result, dp[i] + rdp[i] -1)

print(result)