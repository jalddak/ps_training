tcCnt = int(input())

answer = []
for tc in range(1, tcCnt + 1):
    n = int(input())
    trees = list(map(int, input().split()))
    maxH = max(trees)

    result = 0
    one = 0
    two = 0
    for t in trees:
        h = maxH - t
        one += h % 2
        two += h // 2

    if two - one > 0:
        while abs(two - one) > 1:
            two -= 1
            one += 2

    if one > two:
        result += one * 2 - 1
    elif one == two:
        result += one * 2
    elif one < two:
        result += two * 2



    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))