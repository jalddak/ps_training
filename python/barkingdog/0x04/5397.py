import sys
from collections import deque
def input():
    return sys.stdin.readline().strip()

tc = int(input())
setCmd = set(["<", ">", "-"])

answer = []
for _ in range(tc):
    log = input()
    left = deque()
    right = deque()
    for cmd in log:
        if cmd not in setCmd:
            left.append(cmd)
        elif cmd == "<" and left:
            right.appendleft(left.pop())
        elif cmd == ">" and right:
            left.append(right.popleft())
        elif cmd == "-" and left:
            left.pop()
    answer.append("".join(left + right))

for a in answer:
    print(a)