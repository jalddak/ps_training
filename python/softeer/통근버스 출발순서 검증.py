import sys
n = int(input())
nums = list(map(int, input().split()))

result = 0
for i in range(n):
    stack = 0
    for j in range(i+1, n):
        if nums[i] < nums[j]:
            stack += 1
        if nums[i] > nums[j]:
            result += stack

print(result)