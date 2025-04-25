ip = input()

result = []
expression = ["+", "-", "*", "/", "(", ")"]
stack = []
rank = {"+" : 1, "-" : 1, "*" : 2, "/" : 2}

for a in ip:
    if a not in expression:
        result.append(a)
        continue
    if a == ")":
        while stack[-1] != "(":
            result.append(stack.pop())
        stack.pop()
        continue
    while stack and a != "(" and stack[-1] != "(" and rank[stack[-1]] >= rank[a]:
        result.append(stack.pop())
    stack.append(a)


while stack:
    result.append(stack.pop())


print("".join(result))