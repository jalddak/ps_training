N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

i = N - 1
result = 0
while K > 0:
    if coins[i] <= K:
        cnt = K // coins[i]
        result += cnt
        K -= cnt * coins[i]
    i -= 1

print(result)