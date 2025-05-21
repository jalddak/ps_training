import sys
def input():
    return sys.stdin.readline().strip()

stack = []

n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
