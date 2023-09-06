N = int(input())
A = list(map(int, input().split()))

dp = [[A[0], A[0]]]

for i in range(1, N):
    check = 0
    for n, s in dp:
        if A[i] > n:
            dp.append([A[i], s+A[i]])
            check = 1
            break
    if check == 0:
        dp.append([A[i], A[i]])
    dp.sort(key=lambda x: -x[1])
print(dp[0][1])