import sys
input = sys.stdin.readline

T = int(input())

results = []
for _ in range(T):
    N = int(input())
    hs = input().split()
    if N > 32:
        results.append(0)
        continue
    distances = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i, N):
            for d in range(4):
                if hs[i][d] != hs[j][d]:
                    distances[i][j] += 1
                    distances[j][i] += 1

    s = 1
    n = 12
    while s < N:
        for i in range(s, N):
            for j in range(i+1, N):
                n = min(n, distances[s-1][i] + distances[s-1][j] + distances[i][j])
        s += 1
    results.append(n)


for r in results:
    print(r)