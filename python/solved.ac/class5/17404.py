N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def solution(start):
    global board, N
    dp = [0 for _ in range(3)]
    dp[start] = board[0][start]
    
    for r in range(1, N):
        ndp = [0 for _ in range(3)]
        for i in range(3):
            min_before = 1000 * 1000 + 1
            for j in range(3):
                if dp[j] == 0:
                    continue
                if j == i:
                    continue
                min_before = min(min_before, dp[j])
            ndp[i] = board[r][i] + min_before
        dp = ndp
    result = 1000 * 1000 + 1
    for i in range(3):
        if i == start:
            continue
        result = min(result, dp[i])
    return result



result = 0
for i in range(3):
    if i == 0:
        result = solution(i)
    else:
        result = min(result, solution(i))

print(result)