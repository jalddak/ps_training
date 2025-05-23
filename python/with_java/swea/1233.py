# import sys
# sys.stdin = open('./python/with_java/swea/input.txt', 'r')
# sys.stdout = open('./python/with_java/swea/output.txt', 'w')

tcCnt = 10

answer = []
for tc in range(1, tcCnt+1):
    n = int(input())

    result = 1
    for _ in range(n):
        info = input().split()
        if (len(info) == 2 and not info[1].isdigit()) or (len(info) == 4 and info[1].isdigit()):
            result = 0


    sb = "#" + str(tc) + " " + str(result)
    answer.append(sb)

print("\n".join(answer))