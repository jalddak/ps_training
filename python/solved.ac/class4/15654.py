from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

results = list(permutations(nums, M))
results.sort()

for result in results:
    result = map(str, result)
    print(" ".join(result))