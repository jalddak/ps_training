import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sums = {}
for i in range(N-1):
    for j in range(i+1, N):
        if nums[i] + nums[j] not in sums:
            sums[nums[i] + nums[j]] = [[i, j]]
        else:
            sums[nums[i] + nums[j]].append([i, j])

answer = 0
for i in range(N):
    num = nums[i]
    if num in sums:
        for loca in sums[num]:
            if i not in loca:
                answer += 1
                break

print(answer)

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

answer = 0
for i in range(N):
    nums_ex_i = nums[:i] + nums[i+1:]
    l, r = 0, N-2
    while l < r:
        sumlr = nums_ex_i[l] + nums_ex_i[r]
        if sumlr == nums[i]:
            answer += 1
            break
        elif sumlr < nums[i]:
            l += 1
        else:
            r -= 1

print(answer)