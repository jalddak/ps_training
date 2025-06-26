n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

def back(depth, result):
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(n):
        result.append(nums[i])
        back(depth + 1, result)
        result.pop()


back(0, [])
for a in answer:
    print(a)