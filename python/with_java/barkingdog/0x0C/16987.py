n = int(input())

eggInfo = [list(map(int, input().split())) for _ in range(n)]

answer = 0
def recursion(depth, cnt):
    global answer
    
    if depth == n:
        answer = max(answer, cnt)
        return
    
    for i in range(n):
        if i == depth or eggInfo[depth][0] <= 0:
            recursion(depth + 1, cnt)
            continue
        if eggInfo[i][0] <= 0:
            continue
        
        eggInfo[depth][0] -= eggInfo[i][1]
        cnt += 1 if eggInfo[depth][0] <= 0 else 0
        eggInfo[i][0] -= eggInfo[depth][1]
        cnt += 1 if eggInfo[i][0] <= 0 else 0
        recursion(depth + 1, cnt)
        cnt -= 1 if eggInfo[i][0] <= 0 and eggInfo[i][0] + eggInfo[depth][1] > 0 else 0
        eggInfo[i][0] += eggInfo[depth][1]
        cnt -= 1 if eggInfo[depth][0] <= 0 and eggInfo[depth][0] + eggInfo[i][1] > 0 else 0
        eggInfo[depth][0] += eggInfo[i][1]


recursion(0, 0)

print(answer)