import sys
input = sys.stdin.readline

N = int(input())

l = [int(input()) for _ in range(N)]

result = []

before = [i for i in range(N, 0, -1)]
stack = []
after = []

while len(after) != N:
    num = l[len(after)]
    if len(before) > 0 and num >= before[-1]:
        stack.append(before.pop())
        result.append('+')
    else:
        if stack[-1] != num:
            print("NO")
            exit()
        after.append(stack.pop())
        result.append('-')

for r in result:
    print(r)