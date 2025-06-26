n, m = map(int, input().split())
nums = list(map(int, input().split()))
check = {}

for num in nums:
    check[num] = check[num] + 1 if num in check else 1

nums = sorted(set(nums))
n = len(nums)
answer = []



def back(depth, result):
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(n):
        if check[nums[i]] == 0:
            continue
        check[nums[i]] -= 1
        result.append(nums[i])
        back(depth + 1, result)
        result.pop()
        check[nums[i]] += 1

back(0, [])
for a in answer:
    print(a)