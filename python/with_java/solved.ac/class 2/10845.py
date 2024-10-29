import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
answer = []
q = deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        num = cmd[1]
        q.append(num)
    elif cmd[0] == "pop":
        if q:
            answer.append(q.popleft())
        else:
            answer.append(-1)
    elif cmd[0] == "size":
        answer.append(len(q))
    elif cmd[0] == "empty":
        if q:
            answer.append(0)
        else:
            answer.append(1)
    elif cmd[0] == "front":
        if q:
            answer.append(q[0])
        else:
            answer.append(-1)
    elif cmd[0] == "back":
        if q:
            answer.append(q[-1])
        else:
            answer.append(-1)

for num in answer:
    print(num)