tcCnt = int(input())

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    preSum = [0 for _ in range(5001)]
    for _ in range(n):
        a, b = map(int, input().split())
        preSum[a] += 1
        if b+1 > 5000:
            continue
        preSum[b+1] -= 1

    for i in range(1, 5001):
        preSum[i] += preSum[i-1]

    result = []
    p = int(input())
    for _ in range(p):
        result.append(preSum[int(input())])

    sb = "#" + str(tc) + " " + " ".join(map(str, result))
    answer.append(sb)
print("\n".join(answer))