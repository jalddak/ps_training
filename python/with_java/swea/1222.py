tcCnt = 10

answer = []
for tc in range(1, tcCnt+1):
    n = int(input())
    result = sum(map(int, input().split('+')))
    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)
print("\n".join(answer))