import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())
bhs = [int(input()) for _ in range(n)]

stack = []
cnt = 0
for h in bhs:
    while stack and stack[-1] <= h:
        stack.pop()
    cnt += len(stack)
    stack.append(h)


print(cnt)