s = input()
n = len(s)
stack = []

result = 0
i = 0
while i < n:
    a = s[i]
    if a == "(":
        stack.append(a)
        i += 1
        continue
    stack.pop()
    i += 1
    result += len(stack)
    while i < n and s[i] == ")":
        stack.pop()
        i += 1
        result += 1

print(result)