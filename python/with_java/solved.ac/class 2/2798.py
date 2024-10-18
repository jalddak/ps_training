from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
comb = list(combinations(nums, 3))
candidate = list(map(sum, comb))
candidate.sort()
answer = 0
for c in candidate:
    if m >= c:
        answer = c
print(answer)