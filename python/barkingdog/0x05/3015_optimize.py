import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())

stack = []
cnt = 0
for _ in range(n):
    h = int(input())
    tmp = 1
    while stack and stack[-1][0] <= h:
        if stack[-1][0] == h:
            tmp += stack[-1][1]
        cnt += stack[-1][1]
        stack.pop()
    cnt += 1 if stack else 0

    stack.append([h, tmp])

print(cnt)