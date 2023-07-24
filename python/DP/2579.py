n = int(input())

stair = [int(input()) for _ in range(n)]

dp = [[0, stair[0]]]
for i in range(1, len(stair)):
    next = [0, 0, 0]
    before = dp[i-1]
    for j in range(len(before)):
        if j == 0:
            next[1] += before[0] + stair[i]
        if j == 1:
            next[2] += before[1] + stair[i]
            next[0] = before[1]
        if j == 2:
            next[0] = max(next[0], before[2])
    dp.append(next)

if n >= 2:
    print(max(dp[-1][1], dp[-1][2]))
else:
    print(stair[0])