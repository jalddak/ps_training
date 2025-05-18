dp = [0, 0, 3]

N = int(input())

for i in range(3, N+1):
    if i % 2 == 1:
        dp.append(0)
    else:
        num = 0
        i -= 2
        num += dp[i] * 3
        while i > 2:
            i -= 2
            num += dp[i] * 2
        num += 2
        dp.append(num)

print(dp[N])