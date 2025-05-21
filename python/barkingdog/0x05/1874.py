import sys
def input():
    return sys.stdin.readline().strip()

n = int(input())

nums = [i for i in range(n, 0, -1)]
stack = []
answer = []
for _ in range(n):
    num = int(input())
    while nums and nums[-1] <= num:
        stack.append(nums.pop())
        answer.append("+")
    if stack and stack[-1] == num:
        stack.pop()
        answer.append("-")

if not stack:
    for a in answer:
        print(a)
else:
    print("NO")