n = int(input())
nums = list(map(int, input().split()))
reversedNums = list(reversed(nums))

dp = [[], []]

def check(num, arr, index):
    return arr[index] >= num

def bs(l, r, num, arr):
    while l + 1 < r:
        mid = (l + r) // 2
        if check(num, arr, mid):
            r = mid
        else:
            l = mid

    if r == len(arr):
        arr.append(num)
    arr[r] = num

answer = [0 for _ in range(n)]
for i in range(n):
    bs(-1, len(dp[0]), nums[i], dp[0])
    bs(-1, len(dp[1]), reversedNums[i], dp[1])
    answer[i] += len(dp[0])
    answer[n-i-1] += len(dp[1])

print(max(answer)-1)
