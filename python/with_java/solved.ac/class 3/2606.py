import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a1, a2 = map(int, input().split())
    g[a1].append(a2)
    g[a2].append(a1)

answer = set([1])
temp = [1]

while temp:
    l = temp.pop()
    for c in g[l]:
        if c in answer:
            continue
        else:
            temp.append(c)
            answer.add(c)

print(len(answer) - 1)