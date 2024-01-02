N, M = map(int, input().split())

childs = [set([]) for _ in range(N+1)]
pcnt = [0 for _ in range(N+1)]

for _ in range(M):
    pd = list(map(int, input().split()))
    n = pd[0]
    for i in range(1, n):
        p, c = pd[i], pd[i+1]
        if c not in childs[p]:
            childs[p].add(c)
            pcnt[c] += 1

from collections import deque
queue = deque([])

for i in range(1, N+1):
    if pcnt[i] == 0:
        queue.append(i)

result = []
while queue:
    n = queue.popleft()
    result.append(n)
    for child in childs[n]:
        pcnt[child] -= 1
        if pcnt[child] == 0:
            queue.append(child)

if len(result) != N:
    print(0)
    exit()

for r in result:
    print(r)