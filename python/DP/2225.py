N, K = list(map(int, input().split()))

NUM = 1000000000

if K == 1:
    print(1)
    exit()

dp = [[0 for _ in range(N+2)]]
dp[0][N+1] = 1
for _ in range(2, K):
    before = dp.pop()
    next = [0 for _ in range(N+2)]
    for i in range(1, N+2):
        for j in range(i, N+2):
            next[i] += before[j]
    dp.append(next)

result = 0
final = dp.pop()
for i in range(1, N+2):
    result += i * final[i]
result %= NUM
print(result)