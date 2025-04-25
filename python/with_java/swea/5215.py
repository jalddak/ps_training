# dp
tcCnt = int(input())

answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    n, l = map(int, input().split())

    dp = [0 for _ in range(l + 1)]
    for _ in range(n):
        t, k = map(int, input().split())
        for i in range(l, k-1, -1):
            dp[i] = max(dp[i], dp[i-k] + t)

    sb += str(dp[l])
    answer.append(sb)

for a in answer:
    print(a)

# 백트래킹
tcCnt = int(input())

result = 0
def backTracking(n, l, infos, cur, score, weights):
    global result

    flag = False
    for i in range(cur, n):
        if weights + infos[i][1] > l:
            continue
        flag = True
        weights += infos[i][1]
        score += infos[i][0]
        backTracking(n, l, infos, i + 1, score, weights)
        score -= infos[i][0]
        weights -= infos[i][1]
    
    if not flag:
        result = max(result, score)



answer = []
for tc in range(1, tcCnt+1):
    sb = "#" + str(tc) + " "
    result = 0
    n, l = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(n)]

    backTracking(n, l, infos, 0, 0, 0)
    sb += str(result)
    answer.append(sb)

for a in answer:
    print(a)
    

