n = int(input())
nums = list(map(int, input().split()))
cnts = [0 for _ in range(1000001)]
checked = [False for _ in range(1000001)]
for num in nums:
    checked[num] = True

for num in nums:
    for target in range(num * 2, 1000001, num):
        if not checked[target]:
            continue
        cnts[target] -= 1
        cnts[num] += 1

result = []
for num in nums:
    result.append(cnts[num])

print(" ".join(map(str, result)))