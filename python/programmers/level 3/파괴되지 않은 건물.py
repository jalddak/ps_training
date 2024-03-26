def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for t, r1, c1, r2, c2, d in skill:
        d = -d if t==1 else d
        dp[r1][c1] += d
        if r2+1 < n:
            dp[r2+1][c1] += -d
        if c2+1 < m:
            dp[r1][c2+1] += -d
        if r2+1 < n and c2+1 < m:
            dp[r2+1][c2+1] += d
        
    for i in range(n):
        for j in range(1, m):
            dp[i][j] += dp[i][j-1]
    
    for j in range(m):
        for i in range(1, n):
            dp[i][j] += dp[i-1][j]
    
    broken = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + dp[i][j] <= 0:
                broken += 1
    
    answer = n*m-broken
    
    return answer