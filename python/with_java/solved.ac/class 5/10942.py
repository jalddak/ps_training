import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

m = int(input())

dp = [[True for _ in range(n)] for _ in range(n)]

for i in range(n-1):
    if nums[i] != nums[i+1]:
        dp[i][i+1] = False

for j in range(2, n):
    for i in range(n-j):
        if nums[i] != nums[i+j] or not dp[i+1][i+j-1]:
            dp[i][i+j] = False

answer = []
for _ in range(m):
    s, e = map(lambda x: x-1, map(int, input().split()))
    if dp[s][e]:
        answer.append(1)
    else:
        answer.append(0)

for a in answer:
    print(a)