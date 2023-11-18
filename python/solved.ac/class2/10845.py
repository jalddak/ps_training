import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
result = []
queue = deque([])
for _ in range(T):
    command = input().split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue.popleft())
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == "front":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
    elif command[0] == "back":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1])

for n in result:
    print(n)