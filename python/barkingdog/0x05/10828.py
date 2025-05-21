import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())

stack = []
answer = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    if cmd[0] == "pop":
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)
    if cmd[0] == "size":
        answer.append(len(stack))
    if cmd[0] == "empty":
        if stack:
            answer.append(0)
        else:
            answer.append(1)
    if cmd[0] == "top":
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)

for a in answer:
    print(a)