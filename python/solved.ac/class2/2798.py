from itertools import combinations

N, M = map(int, input().split())
l = list(map(int, input().split()))

candidates = list(map(sum, list(combinations(l, 3))))
candidates.sort(reverse=True)

for n in candidates:
    if n <= M:
        print(n)
        exit()