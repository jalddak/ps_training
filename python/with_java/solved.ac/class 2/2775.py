t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [([0 for _ in range(n+1)]) for _ in range(k+1)]
    apt[0] = [i for i in range(n+1)]
    for f in range(1, k+1):
        s = 0
        for r in range(1, n+1):
            s += apt[f-1][r]
            apt[f][r] = s
    print(apt[k][n])