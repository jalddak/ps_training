N = int(input())
nums = list(map(int, input().split()))

s, b = 0, N-1
find = 1000000000 * 2
results = 0
resultb = 0
while s < b:
    temp = nums[s] + nums[b]
    if abs(temp) < find:
        results = s
        resultb = b
        find = abs(temp)
    if temp < 0:
        s += 1
    else:
        b -= 1

print(nums[results], nums[resultb])