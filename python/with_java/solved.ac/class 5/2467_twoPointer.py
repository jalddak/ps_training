n = int(input())
nums = list(map(int, input().split()))

minAbsSum = 1000000000 * 2 + 1

s, e = 0, n-1
result = []

while s < e:
    sum = nums[s] + nums[e]
    if abs(sum) < minAbsSum:
        minAbsSum = abs(sum)
        result = [nums[s], nums[e]]
    if sum < 0:
        s += 1
    elif sum > 0:
        e -= 1
    else:
        break

print(result[0], result[1])