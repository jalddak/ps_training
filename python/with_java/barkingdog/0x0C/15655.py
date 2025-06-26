n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

def back(depth, result, start):
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(start, n):
        result.append(nums[i])
        back(depth + 1, result, i + 1)
        result.pop()


back(0, [], 0)
for a in answer:
    print(a)