n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
check = [False for _ in range(n + 1)]
answer = []

def back(depth, result):
    if depth == m:
        answer.append(" ".join(map(str, result)))
        return
    
    for i in range(n):
        if check[i]:
            continue

        check[i] = True
        result.append(nums[i])
        back(depth + 1, result)
        result.pop()
        check[i] = False


back(0, [])
for a in answer:
    print(a)