# import sys
# sys.setrecursionlimit(10**6)

n = int(input())

answer = 0
dp = [-1 for _ in range(n+1)]
dp[1] = 0

for i in range(2, n+1):
    candidate = []
    if i % 3 == 0:
        candidate.append(dp[i//3])
    if i % 2 == 0:
        candidate.append(dp[i//2])
    candidate.append(dp[i-1])
    dp[i] = min(candidate) + 1

print(dp[n])

# def memo(n):
#     if dp[n] == -1:
#         candidate = []
#         if n % 3 == 0:
#             candidate.append(memo(n//3))
#         if n % 2 == 0:
#             candidate.append(memo(n//2))
#         candidate.append(memo(n-1))
#         result = min(candidate) + 1
#         dp[n] = result
#     return dp[n]

# memo(n)
# print(dp[n])