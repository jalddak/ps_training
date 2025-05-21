import sys
def input():
    return sys.stdin.readline().strip()

t = int(input())

answer = []
for _ in range(t):
    s = input()
    stack = []
    result = "YES"
    for a in s:
        if a == "(" or a == "[":
            stack.append(a)
        elif not stack or (a == ")" and stack[-1] != "(") or (a == "]" and stack[-1] != "["):
            result = "NO"
            break
        else:
            stack.pop()
    if stack:
        result = "NO"
    answer.append(result)

print("\n".join(answer))