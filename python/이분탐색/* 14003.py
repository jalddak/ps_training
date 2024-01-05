N = int(input())
nums = list(map(int, input().split()))
def binary_search(l, n):
    min_index = 0
    max_index = len(l)-1

    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if n <= l[mid_index]:
            max_index = mid_index
        else:
            min_index = mid_index + 1
    
    return min_index

dp = [nums[0]]
nums_info = [(nums[0], 0)]
max_index = 0

for i in range(1, N):
    num = nums[i]
    index = binary_search(dp, num)
    if index == len(dp)-1 and dp[-1] < num:
        dp.append(num)
        index += 1
        max_index = index
    else: dp[index] = num
    nums_info.append((num, index))

result = []
temp = max_index
for i in range(N-1, -1, -1):
    num, index = nums_info[i]
    if temp == index:
        temp -= 1
        result.append(num)
    if temp < 0:
        break
result.reverse()

print(max_index+1)
print(" ".join(map(str, result)))
    
# 시간 초과
N = int(input())

nums = list(map(int, input().split()))

def binary_search(l, n):
    min_index = 0
    max_index = len(l)-1

    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if n <= l[mid_index]:
            max_index = mid_index
        else:
            min_index = mid_index + 1
    
    return min_index

dp = []
for num in nums:
    isMin = True
    for i in range(len(dp)):
        candidate = dp[i]
        if num < candidate[-1]:
            index = binary_search(candidate, num)
            if i < len(dp)-1 and index + 1 > len(dp[i+1]):
                isMin = False
                next = candidate[:index]+[num]
                dp.insert(i+1, next)
                if len(candidate) <= len(next):
                    dp.pop(i)
                break
        if num == candidate[-1]:
            isMin = False
            break
        if num > candidate[-1]:
            candidate.append(num)
            isMin = False
            if i > 0 and len(candidate) >= len(dp[i-1]):
                dp.pop(i-1)
            break
    if isMin:
        if not dp:
            dp.append([num])
            continue
        index = binary_search(dp[-1], num)
        next = dp[-1][:index] + [num]
        if len(dp[-1]) <= len(next):
            dp.pop()
        dp.append(next)

print(len(dp[0]))
print(" ".join(map(str, dp[0])))