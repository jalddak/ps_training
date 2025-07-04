n, m = map(int, input().split())
nums = list(set(map(int, input().split())))
nums.sort()

result = []
answer = []

def recursion(depth):
    global n, m, nums, info

    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for num in nums:
        result.append(num)
        recursion(depth + 1)
        result.pop()

recursion(0)
for a in answer:
    print(a)