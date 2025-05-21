import sys
def input():
    return sys.stdin.readline().strip()

answer = []

while True:
    ip = list(map(int, input().split()))
    if ip[0] == 0:
        break

    n = ip[0]
    ip.append(0)
    stack = []
    result = 0
    for i in range(1, n+2):
        h = ip[i]
        tmp = 0
        while stack and stack[-1][0] > h:
            tmp += stack[-1][1]
            candidate = stack[-1][0] * tmp
            result = max(result, candidate)
            stack.pop()
        stack.append([h, tmp + 1])
    answer.append(result)
print("\n".join(map(str, answer)))