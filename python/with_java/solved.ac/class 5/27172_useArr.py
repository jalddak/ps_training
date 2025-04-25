n = int(input())
nums = list(map(int, input().split()))
cnts = [0 for _ in range(1000001)]

numSet = set(nums)
for num in nums:
    for target in range(num * 2, 1000001, num):
        cnts[target] -= 1
        if target in numSet:
            cnts[num] += 1

result = []
for num in nums:
    result.append(cnts[num])

print(" ".join(map(str, result)))