import sys
input = sys.stdin.readline

N, M = map(int, input().split())

l = list(map(int, input().split()))

dp = [l[0]]

for i in range(1, N):
    dp.append(l[i] + dp[i-1])

for _ in range(M):
    s, e = map(int, input().split())
    if s == 1:
        print(dp[e-1])
    else:
        print(dp[e-1] - dp[s-2])