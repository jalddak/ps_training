n = int(input())

answer = []
for _ in range(n):
    cmd = input()
    flag = True
    stack = []
    for c in cmd:
        if c == "(":
            stack.append(1)
        elif stack:
            stack.pop()
        else:
            flag = False
            break
    if stack:
        flag = False
    if flag:
        answer.append("YES")
    else:
        answer.append("NO")

print("\n".join(answer))