n = int(input())
tops = list(map(int, input().split()))

stack = []
answer = []

for i in range(n):
    t = tops[i]
    while stack and stack[-1][0] < t:
        stack.pop()
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][1])
    stack.append([t, i + 1])

print(*answer)