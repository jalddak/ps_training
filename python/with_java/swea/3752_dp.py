tcCnt = int(input())

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    dp = [False for _ in range(sum(scores) + 1)]
    dp[0] = True

    for score in scores:
        for i in range(len(dp)-1, score-1, -1):
            if dp[i-score] == True:
                dp[i] = True
    
    result = 0
    for i in range(len(dp)):
        if dp[i]:
            result += 1

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))