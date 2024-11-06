import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = set()
answer = []
for _ in range(n):
    s.add(input()[:-1])

for _ in range(m):
    name = input()[:-1]
    if name in s:
        answer.append(name)

answer.sort()
print(len(answer))
for a in answer:
    print(a)