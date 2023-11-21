N = int(input())

l = list(map(int, input().split()))
l.sort()

dp = [l[0]]
for i in range(1, N):
    dp.append(l[i] + dp[i-1])

print(sum(dp))