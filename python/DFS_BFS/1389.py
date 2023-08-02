# BFS

from collections import deque

N, M = list(map(int, input().split()))

tree = {}

for _ in range(M):
    f, s = list(map(int, input().split()))
    if f not in tree:
        tree[f] = [s]
    else:
        tree[f].append(s)
    if s not in tree:
        tree[s] = [f]
    else:
        tree[s].append(f)

score = N*N
result = 0
for key in tree:
    visited = [-1 for _ in range(N)]
    visited[key-1] = 0
    queue = deque([[key, 0]])
    while len(queue) != 0:
        n, cnt = queue.popleft()
        for relation in tree[n]:
            if visited[relation-1] == -1:
                visited[relation-1] = cnt+1
                queue.append([relation, cnt+1])
    n_score = sum(visited)
    if score > n_score:
        score = n_score
        result = key
    elif score == n_score:
        result = min(key, result)

print(result)