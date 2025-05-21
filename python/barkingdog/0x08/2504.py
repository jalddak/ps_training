s = input()

stack = []
flag = True
for a in s:
    if a == "(" or a == "[":
        stack.append(a)
        continue
    elif not stack:
        flag = False
        break
    temp = 0
    if a == ")":
        while stack and isinstance(stack[-1], int):
            temp += stack.pop()
        if not stack or stack[-1] != "(":
            flag = False
            break
        stack.pop()
        if temp == 0:
            stack.append(2)
        else:
            stack.append(temp * 2)
    
    if a == "]":
        while stack and isinstance(stack[-1], int):
            temp += stack.pop()
        if not stack or stack[-1] != "[":
            flag = False
            break
        stack.pop()
        if temp == 0:
            stack.append(3)
        else:
            stack.append(temp * 3)

answer = 0
while stack and isinstance(stack[-1], int):
    answer += stack.pop()

if stack or not flag:
    answer = 0

print(answer)