import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())

hs = [int(input()) for _ in range(n)]
cnts = [0 for _ in range(n)]
stack = []
cnt = 0
for i in range(n):
    h = hs[i]
    cnts[i] += 1
    tmp = 0
    while stack and hs[stack[-1]] <= h:
        if hs[stack[-1]] == h:
            cnts[i] += cnts[stack[-1]]
        tmp += cnts[stack[-1]]
        stack.pop()
    tmp += 1 if stack else 0
    cnt += tmp

    stack.append(i)

print(cnt)