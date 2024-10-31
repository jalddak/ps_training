import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "pop":
        answer.append(stack.pop() if stack else -1)
    elif cmd[0] == "size":
        answer.append(len(stack))
    elif cmd[0] == "empty":
        answer.append(0 if stack else 1)
    elif cmd[0] == "top":
        answer.append(stack[-1] if stack else -1)
    
for a in answer:
    print(a)