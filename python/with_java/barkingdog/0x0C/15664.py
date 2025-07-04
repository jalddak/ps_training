n, m = map(int, input().split())
nums = list(map(int, input().split()))

info = {}
for num in nums:
    info[num] = 1 if num not in info else info[num] + 1

nums = list(info.keys())
nums.sort()

result = []
answer = []
n = len(nums)

def recursion(depth, start):
    global n, m, nums, info

    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(start, n):
        num = nums[i]
        if info[num] < 1:
            continue

        info[num] -= 1
        result.append(num)
        recursion(depth + 1, i)
        result.pop()
        info[num] += 1

recursion(0, 0)
for a in answer:
    print(a)