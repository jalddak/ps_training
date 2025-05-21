n = int(input())

cnt = 0
for _ in range(n):
    s = input()
    stack = []
    for a in s:
        if not stack or stack[-1] != a:
            stack.append(a)
        else:
            stack.pop()
    if not stack:
        cnt += 1

print(cnt)