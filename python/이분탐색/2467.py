N = int(input())

nums = list(map(int, input().split()))
nums.sort()

near_zero = 1000000000 * 2
rsi, rbi = -1, -1
si, bi = 0, N-1

while si < bi:
    mix = nums[si] + nums[bi]
    if abs(mix) < near_zero:
        near_zero = abs(mix)
        rsi, rbi = si, bi
    if mix < 0:
        si += 1
    else:
        bi -= 1

print(nums[rsi], nums[rbi])