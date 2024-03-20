def solution(sequence):
    answer = 0
    dp = [0, 0]
    for n in sequence:
        a, b = n, -n
        t1, t2 = dp
        dp[0] = max(t2+a, a)
        dp[1] = max(t1+b, b)
        answer = max(answer, dp[0], dp[1])
    return answer