import sys
input = sys.stdin.readline

T = int(input())

answer = []
for _ in range(T):
    N = int(input())
    humans = [list(map(int, input().split())) for _ in range(N)]
    humans.sort(key=lambda x:(x[0], x[1]))
    result = 1
    cutline = humans[0][1]
    for i in range(1, N):
        if humans[i][1] < cutline:
            cutline = humans[i][1]
            result += 1

    answer.append(result)

for a in answer:
    print(a)