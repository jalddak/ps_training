n, k = map(int, input().split())

info = [[0 for _ in range(6)] for _ in range(2)]
for _ in range(n):
    s, y = map(int, input().split())
    info[s][y-1] += 1

answer = 0
for i in range(2):
    for j in range(6):
        answer += info[i][j] // k + (1 if info[i][j] % k != 0 else 0)

print(answer)

