n, k = list(map(int, input().split()))

coin = [int(input()) for _ in range(n)]

visited = [False for _ in range(k)]
dp = {0: [k]}

i = 0
while i in dp:
    i += 1
    for need in dp[i-1]:
        for c in coin:
            n_need = need - c
            if n_need == 0:
                print(i)
                quit()
            if n_need > 0 and not visited[n_need]:
                visited[n_need] = True
                if i not in dp:
                    dp[i] = [n_need]
                else:
                    dp[i].append(n_need)

print(-1)