n = int(input())
nums = list(map(int, input().split()))

dp = [nums[0]]

def bs(num):
    global dp
    min_i = 0
    max_i = len(dp) - 1
    result = max_i
    while min_i <= max_i:
        mid = (min_i + max_i) // 2
        if dp[mid] < num:
            min_i = mid + 1
        elif dp[mid] > num:
            result = mid
            max_i = mid - 1
        else:
            result = mid
            break
    return result

for i in range(1, n):
    if dp[-1] < nums[i]:
        dp.append(nums[i])
    else:
        dp[bs(nums[i])] = nums[i]

print(len(dp))