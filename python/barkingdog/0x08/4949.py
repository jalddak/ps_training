import sys
def input():
    return sys.stdin.readline()

answer = []
while True:
    s = input()
    if s == ".\n":
        break

    stack = []
    result = "yes"
    for a in s:
        if a == "(" or a == "[":
            stack.append(a)
        elif a == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                result = "no"
                break
        elif a == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                result = "no"
                break
    if stack:
        result = "no"
    answer.append(result)

print("\n".join(answer))