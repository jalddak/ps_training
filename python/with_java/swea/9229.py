tcCnt = int(input())

answer = []
for tc in range(1, tcCnt + 1):
    n, m = map(int, input().split())
    ws = list(map(int, input().split()))

    ws.sort()
    result = -1
    l = 0
    r = n - 1
    while l < r:
        temp = ws[l] + ws[r]
        if temp == m:
            result = temp
            break
        elif temp > m:
            r -= 1
        else:
            result = max(result, temp)
            l += 1


    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))