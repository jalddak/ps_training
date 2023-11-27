import sys
input = sys.stdin.readline

T = int(input())
P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
results = []
for _ in range(T):
    n = int(input())
    if n < len(P):
        results.append(P[n])
        continue
    index = len(P)-1
    while len(P) < n+1:
        P.append(P[-1] + P[-5])
    results.append(P[n])

for r in results:
    print(r)