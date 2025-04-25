import sys
input = sys.stdin.readline

n = int(input())

n1, n2, n3 = map(int, input().split())
dp = [[n1, n2, n3], [n1, n2, n3]]

for _ in range(1, n):
    n1, n2, n3 = map(int, input().split())
    
    temp = [
        [min(dp[0][:2]) + n1, min(dp[0]) + n2, min(dp[0][1:]) + n3]
        , [max(dp[1][:2]) + n1, max(dp[1]) + n2, max(dp[1][1:]) + n3]
    ]
    dp = temp

print(max(dp[1]), min(dp[0]))