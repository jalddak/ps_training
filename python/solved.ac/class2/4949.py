result = []
while True:
    sentence = input()
    if sentence == ".":
        break
    stack = []
    flag = True
    for c in sentence:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif c == "[":
            stack.append(c)
        elif c == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    if len(stack) == 0 and flag:
        result.append("yes")
    else:
        result.append("no")

for r in result:
    print(r)