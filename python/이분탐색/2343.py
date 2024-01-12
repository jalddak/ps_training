import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

min_t = max(nums)-1
max_t = sum(nums)

while min_t + 1 < max_t:
    mid = (min_t + max_t) // 2

    temp = 0
    cnt = 1
    for n in nums:
        if temp + n <= mid:
            temp += n
        else:
            temp = n
            cnt += 1

    if cnt > M:
        min_t = mid
    else:
        max_t = mid

print(max_t)
