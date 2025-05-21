n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

l, r = 0, len(nums)-1

cnt = 0
while l < r:
    if nums[l] + nums[r] < x:
        l += 1
    elif nums[l] + nums[r] > x:
        r -= 1
    else:
        cnt += 1
        r -= 1
print(cnt)