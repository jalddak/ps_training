# n, k = map(int, input().split())

# u = 1
# d = 1
# for i in range(1, n+1):
#     u *= i
# for i in range(1, k+1):
#     d *= i
# for i in range(1, n-k+1):
#     d *= i

# print(u // d)

n, k = map(int, input().split())

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] * i

print(dp[n] // (dp[n-k] * dp[k]))