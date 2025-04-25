import sys
input = sys.stdin.readline

t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    sts = [list(map(int, input().split())) for _ in range(2)]
    dp = [sts[0][0], sts[1][0], 0]
    for i in range(1, n):
        temp = [max(dp[1], dp[2]) + sts[0][i]
                , max(dp[0], dp[2]) + sts[1][i]
                , max(dp[0], dp[1])]
        dp = temp
    answer.append(max(dp))

for a in answer:
    print(a)