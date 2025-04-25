n = int(input())
nums = list(map(int, input().split()))

# 1번째 방법
dp = [nums[0]]

def bs(arr, num, s, e):
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] > num:
            e = mid - 1
        elif arr[mid] < num:
            s = mid + 1
        else:
            return mid
    return s

for i in range(1, n):
    num = nums[i]
    length = len(dp)
    index = bs(dp, num, 0, length-1)
    if index == length:
        dp.append(num)
    elif dp[index] > num:
        dp[index] = num

print(len(dp))

# 2번쨰 방법
dp = []

def bs(arr, num, s, e):
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] > num:
            e = mid - 1
        elif arr[mid] < num:
            s = mid + 1
        else:
            return
    arr[s] = num

for i in range(n):
    if not dp or dp[-1] < nums[i]:
        dp.append(nums[i])
        continue
    bs(dp, nums[i], 0, len(dp)-1)

print(len(dp))

# 3번쨰 방법
dp = []

def check(arr, index, num):
    return arr[index] >= num

def bs(arr, num, s, e):
    while s + 1 < e:
        mid = (s + e) // 2

        if check(arr, mid, num):
            e = mid
        else:
            s = mid

    arr[e] = num

for i in range(n):
    if not dp or dp[-1] < nums[i]:
        dp.append(nums[i])
        continue
    if dp and dp[0] >= nums[i]:
        dp[0] = nums[i]
        continue
    bs(dp, nums[i], 0, len(dp)-1)

print(len(dp))

# 4번쨰 방법
dp = []

def check(arr, index, num):
    return arr[index] >= num

def bs(arr, num, s, e):
    while s + 1 < e:
        mid = (s + e) // 2

        if check(arr, mid, num):
            e = mid
        else:
            s = mid

    if e == len(arr):
        arr.append(num)
        return
    arr[e] = num

for i in range(n):
    bs(dp, nums[i], -1, len(dp))

print(len(dp))