import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
    if i < N-1:
        if nums[i] == nums[i+1]:
            dp[i][i+1] = 1
        else:
            dp[i][i+1] = 0

def check(s, e):
    global dp, nums
    if nums[s] != nums[e] or dp[s+1][e-1] == 0:
        dp[s][e] = 0
    elif dp[s+1][e-1] == 1:
        dp[s][e] = 1
    elif dp[s+1][e-1] == -1:
        check(s+1, e-1)
        dp[s][e] = dp[s+1][e-1]

results = []
for _ in range(M):
    S, E = map(lambda x:x-1, map(int, input().split()))
    if dp[S][E] == -1:
        check(S, E)
    results.append(dp[S][E])


for r in results:
    print(r)

    