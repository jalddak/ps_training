import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

left = deque(list(input()))
right = deque()

m = int(input())

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "L" and left:
        right.appendleft(left.pop())
    if cmd[0] == "D" and right:
        left.append(right.popleft())
    if cmd[0] == "B" and left:
        left.pop()
    if cmd[0] == "P":
        left.append(cmd[1])


answer = "".join(left) + "".join(right)
print(answer)