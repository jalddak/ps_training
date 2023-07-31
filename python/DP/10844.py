n = int(input())

dp = [[1 for _ in range(10)]]

dp[0][0] = 0

for i in range(1, n):
    before = dp[i-1]
    next = [0 for _ in range(10)]
    for j in range(len(before)):
        if j == 0:
            next[j+1] += before[j]
        elif j == 9:
            next[j-1] += before[j]
        else:
            next[j+1] += before[j]
            next[j-1] += before[j]
    dp.append(next)

print(sum(dp[-1]) % 1000000000)