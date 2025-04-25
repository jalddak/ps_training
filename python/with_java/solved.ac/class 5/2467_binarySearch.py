n = int(input())
nums = list(map(int, input().split()))

minAbsSum = 1000000000 * 2 + 1
result = []

def check(arr, target, index):
    return arr[target] + arr[index] >= 0

def bs(l, r, arr, target):
    global minAbsSum, result
    while l + 1 < r:
        mid = (l + r) // 2
        temp = arr[target] + arr[mid]
        if abs(temp) < minAbsSum:
            minAbsSum = abs(temp)
            result = [arr[target], arr[mid]]
        
        if check(arr, target, mid):
            r = mid
        else:
            l = mid

for i in range(n-1):
    bs(i, n, nums, i)
    if sum(result) == 0:
        break

print(result[0], result[1])