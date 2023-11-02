from itertools import combinations

N, S = map(int, input().split())

l = list(map(int, input().split()))

result = 0
for i in range(1, N+1):
    subl = list(combinations(l, i))
    for sub in subl:
        if sum(sub) == S:
            result += 1

print(result)