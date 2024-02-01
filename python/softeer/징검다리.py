import sys

N = int(input())
hs = list(map(int, input().split()))

dp = [hs[0]]

def bs(dp, h):
    l, r = 0, len(dp)-1
    while l <= r:
        m = (l+r) // 2
        if h == dp[m]:
            return m
        elif h > dp[m]:
            l = m + 1
        else:
            r = m - 1
    return l

for i in range(1, N):
    if hs[i] > dp[-1]:
        dp.append(hs[i])
    else:
        dp[bs(dp, hs[i])] = hs[i]

print(len(dp))
        