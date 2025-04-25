n, m, r = map(int, input().split())
t = [0] + list(map(int, input().split()))

edges = [[16 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    edges[i][i] = 0
for _ in range(r):
    s, e, distance = map(int, input().split())
    if edges[s][e] <= distance:
        continue
    edges[s][e] = distance
    edges[e][s] = distance

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            edges[i][j] = min(edges[i][j], edges[i][k] + edges[k][j])

answer = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if edges[i][j] > m:
            continue
        temp += t[j]
    answer = max(answer, temp)

print(answer)