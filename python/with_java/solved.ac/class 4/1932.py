import sys
input = sys.stdin.readline

n = int(input())
dp = [int(input())]

for i in range(1, n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if j == 0:
            temp[j] += dp[j]
        elif j == i:
            temp[j] += dp[j-1]
        else:
            temp[j] += max(dp[j-1], dp[j])
    dp = temp

print(max(dp))