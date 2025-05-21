import sys
from collections import deque
def input():
    return sys.stdin.readline().strip()

n = int(input())
q = deque()
answer = []

for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        if not q:
            answer.append(-1)
        else:
            answer.append(q.popleft())
    elif cmd[0] == "size":
        answer.append(len(q))
    elif cmd[0] == "empty":
        if not q:
            answer.append(1)
        else:
            answer.append(0)
    elif cmd[0] == "front":
        if not q:
            answer.append(-1)
        else:
            answer.append(q[0])
    elif cmd[0] == "back":
        if not q:
            answer.append(-1)
        else:
            answer.append(q[-1])

print("\n".join(map(str, answer)))