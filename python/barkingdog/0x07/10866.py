import sys
def input():
    return sys.stdin.readline().strip()

from collections import deque

q = deque()
answer = []

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push_front":
        q.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        q.append(cmd[1])
    elif cmd[0] == "pop_front":
        if not q:
            answer.append(-1)
        else:
            answer.append(q.popleft())
    elif cmd[0] == "pop_back":
        if not q:
            answer.append(-1)
        else:
            answer.append(q.pop())
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