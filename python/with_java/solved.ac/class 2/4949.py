import sys
input = sys.stdin.readline

answer = []
while True:
    string = input()
    stack = []
    flag = True
    if string == ".\n":
        break
    for c in string:
        if c in ["(", "["]:
            stack.append(c)
        elif c in [")", "]"]:
            if c == ")" and (stack and stack[-1] == "("):
                stack.pop()
            elif c == "]" and (stack and stack[-1] == "["):
                stack.pop()
            else:
                flag = False
                break

    if stack:
        flag = False
    if flag:
        answer.append("yes")
    else:
        answer.append("no")

print("\n".join(answer))
