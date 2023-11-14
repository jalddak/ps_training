import sys
input = sys.stdin.readline
T = int(input())

result = []
for _ in range(T):
    stack = []
    l = list(input())[:-1]
    for ps in l:
        if ps == '(':
            stack.append(1)
        elif len(stack) != 0:
            stack.pop()
        else:
            stack.append(-1)
            break
    if len(stack) == 0:
        result.append("YES")
    else:
        result.append("NO")

for ans in result:
    print(ans)