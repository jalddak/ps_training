import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [list(map(int, list(input()[:-1]))) for _ in range(n)]

max_len = 0
for y in range(n):
    for x in range(m):
        if y < 1 or x < 1 or dp[y][x] == 0:
            if dp[y][x] == 1 and max_len < 1:
                max_len = 1
            continue
        dp[y][x] = min(dp[y-1][x-1], dp[y-1][x], dp[y][x-1]) + 1
        max_len = max(dp[y][x], max_len)

print(max_len ** 2)