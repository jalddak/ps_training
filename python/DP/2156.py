n = int(input())

l = [int(input()) for _ in range(n)]

dp = [[0, l[0], 0]]

for i in range(1, n):
    before = dp[i-1]
    next = [0, 0, 0]
    next[0] = max(before)
    next[1] = before[0] + l[i]
    next[2] = before[1] + l[i]
    dp.append(next)

print(max(dp[-1]))
