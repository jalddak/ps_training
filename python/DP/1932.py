n = int(input())

tri = [list(map(int, input().split())) for _ in range(n)]
dp = [tri[0]]

for i in range(1, n):
    candidate = [0 for _ in range(i+1)]
    before = dp[i-1]
    for j in range(len(before)):
        candidate[j] = max(candidate[j], before[j]+tri[i][j])
        candidate[j+1] = max(candidate[j+1], before[j]+tri[i][j+1])
    dp.append(candidate)

print(max(dp[-1]))