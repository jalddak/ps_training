import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    M, N, x, y = map(int, input().split())
    last = M * N
    day = x if M > N else y
    temp = M if M > N else N
    flag = False
    while day <= last:
        ex = day % M if day % M != 0 else M
        ey = day % N if day % N != 0 else N
        if ex == x and ey == y:
            flag = True
            result.append(day)
            break
        day += temp
    if not flag:
        result.append(-1)

for n in result:
    print(n)