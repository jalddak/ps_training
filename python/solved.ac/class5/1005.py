import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

results = []
for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    counts = [0 for _ in range(N)]
    childs = [[] for _ in range(N)]
    for _ in range(K):
        p, c = map(lambda x:x-1, map(int, input().split()))
        childs[p].append(c)
        counts[c] += 1
    
    
    cts = times[:]
    queue = deque([])
    for i in range(N):
        if counts[i] == 0:
            queue.append(i)

    check = int(input()) - 1
    while len(queue) != 0:
        node = queue.popleft()
        for child in childs[node]:
            counts[child] -= 1
            cts[child] = max(cts[child], times[child] + cts[node])
            if counts[child] == 0:
                if child == check:
                    breaker = True
                    break
                queue.append(child)
    
    results.append(cts[check])

for r in results:
    print(r)