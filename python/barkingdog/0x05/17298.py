n = int(input())
nums = list(map(int, input().split()))

stack = []
answer = [-1 for _ in range(n)]
for i in range(n):
    num = nums[i]
    while stack and nums[stack[-1]] < num:
        answer[stack.pop()] = num
    stack.append(i)
    
print(*answer)