import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

def bs(dp, n):
    l, r = 0, len(dp)-1

    result = r
    while l <= r:
        m = (l+r) // 2
        if dp[m] < n:
            l = m + 1
        else:
            r = m - 1
            result = m
    
    dp[result] = n

dp = []
for n in nums:
    if not dp or dp[-1] < n:
        dp.append(n)
        continue
    bs(dp, n)

print(len(dp))