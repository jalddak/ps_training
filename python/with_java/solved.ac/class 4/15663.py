n, m = map(int, input().split())
nums = list(map(int, input().split()))
ncnts = dict()
for num in nums:
    ncnts[num] = 1 if num not in ncnts else ncnts[num] + 1

nums = sorted(list(ncnts.keys()))

length = len(nums)
answer = []

def recursion(depth, result):
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return

    for i in range(length):
        if ncnts[nums[i]] < 1:
            continue
        ncnts[nums[i]] -= 1
        result.append(nums[i])
        recursion(depth + 1, result)
        result.pop()
        ncnts[nums[i]] += 1

recursion(0, [])
for a in answer:
    print(a)
