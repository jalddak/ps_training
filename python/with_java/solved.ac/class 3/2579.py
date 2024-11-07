import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]
if n == 1:
    print(stairs[n-1])
    exit()

dp = [[stairs[0], 0], [stairs[1], stairs[0] + stairs[1]]]
for i in range(2, n):
    candidate = []
    candidate.append(max(dp[i-2][0], dp[i-2][1]) + stairs[i])
    candidate.append(dp[i-1][0] + stairs[i])
    dp.append(candidate)

print(max(dp[n-1]))