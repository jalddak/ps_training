def solution(n):
    answer = 0
    dp = []
    for i in range(n+1):
        dp.append(i)
    
    for i in range(1, n+1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        else:
            dp[i] = dp[i-2] + dp[i-1]
    
    answer = dp[n]
    answer %= 1234567
        
    return answer