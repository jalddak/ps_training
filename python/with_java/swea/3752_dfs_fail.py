# dfs는 2의 100제곱 번 계산해야해서 안됨

tcCnt = int(input())

def recursion(n, scores, check, cur, preSum):
    for i in range(cur, n):
        score = preSum + scores[i]
        check.add(score)
        recursion(n, scores, check, i + 1, score)

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    check = set([0])

    recursion(n, scores, check, 0, 0)

    result = len(check)
    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))