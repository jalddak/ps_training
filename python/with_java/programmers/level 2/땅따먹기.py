def solution(land):
    dp = land[0]
    for i in range(1, len(land)):
        ndp = []
        for j in range(4):
            ndp.append(max(dp[0:j] + dp[j+1:4]) + land[i][j])
        dp = ndp
    return max(dp)