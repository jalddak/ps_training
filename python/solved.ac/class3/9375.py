import sys
input = sys.stdin.readline

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    d = {}
    for _ in range(n):
        name, kind = input().split()
        if kind not in d:
            d[kind] = 1
        else:
            d[kind] += 1
    n = 1
    for key in d:
        n *= (d[key] + 1)
    n -= 1
    results.append(n)

for r in results:
    print(r)