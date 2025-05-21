import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())
bhs = [int(input()) for _ in range(n)]
cnts = [0 for _ in range(n)]

stack = []
for i in range(n - 1, -1, -1):
    h = bhs[i]
    while stack and bhs[stack[-1]] < h:
        cnts[i] += cnts[stack.pop()] + 1
    stack.append(i)

print(sum(cnts))