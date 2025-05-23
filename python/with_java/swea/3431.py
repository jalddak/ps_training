tcCnt = int(input())

answer = []
for tc in range(1, tcCnt + 1):
    l, u, x = map(int, input().split())
    result = 0
    if x > u:
        result = -1
    if x < l:
        result = l - x

    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)
print("\n".join(answer))