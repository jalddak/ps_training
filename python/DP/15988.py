import sys
input = sys.stdin.readline

T = int(input())

dp = [0, 1, 2, 4]
result = []
for _ in range(T):
    n = int(input())
    know = len(dp)
    for i in range(know, n+1):
        dp.append((dp[-1] + dp[-2] + dp[-3]) % 1000000009)
    result.append(dp[n])

for r in result:
    print(r)