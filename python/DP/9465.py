T = int(input())

result = []
for _ in range(T):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = []
    for i in range(n):
        if i == 0:
            candidates = [0, 0, 0]
            candidates[0] = board[0][i]
            candidates[1] = board[1][i]
            dp.append(candidates)
            continue

        before = dp[i-1]
        next = [0, 0, 0]
        for index in range(3):
            if index == 0:
                next[1] = max(next[1], before[index]+board[1][i])
                next[2] = max(next[2], before[index])
            elif index == 1:
                next[0] = max(next[0], before[index]+board[0][i])
                next[2] = max(next[2], before[index])
            elif index == 2:
                next[0] = max(next[0], before[index]+board[0][i])
                next[1] = max(next[1], before[index]+board[1][i])
        dp.append(next)
    result.append(max(dp[-1]))

for r in result:
    print(r)