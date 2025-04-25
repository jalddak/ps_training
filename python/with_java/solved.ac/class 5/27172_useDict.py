n = int(input())
nums = list(map(int, input().split()))
numSet = set(nums)

numCnt = dict()
for num in nums:
    numCnt[num] = 0

for num in nums:
    for target in range(num * 2, 1000001, num):
        if target not in numSet:
            continue
        numCnt[target] -= 1
        numCnt[num] += 1

result = []
for num in nums:
    result.append(numCnt[num])

print(" ".join(map(str, result)))