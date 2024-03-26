# dp 아이디어 체크

def solution(n, money):
    answer = 0
    dp = [0 for _ in range(n+1)]
    for coin in money:
        dp[coin] += 1
        for price in range(coin+1, n+1):
            dp[price] += dp[price-coin]
    answer = dp[-1]
    return answer