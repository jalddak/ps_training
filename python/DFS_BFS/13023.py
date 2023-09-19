import sys
sys.setrecursionlimit(10 ** 4)

N, M = list(map(int, input().split()))

node = {}
for _ in range(M):
    f, s = list(map(int, input().split()))
    if f not in node:
        node[f] = [s]
    else:
        node[f].append(s)

    if s not in node:
        node[s] = [f]
    else:
        node[s].append(f)

visited = [0 for _ in range(N)]

def dfs(n, cnt):
    global node, visited
    visited[n] = 1
    result = cnt
    if n in node and result < 5:
        for h in node[n]:
            if visited[h] == 0:
                result = max(result, dfs(h, cnt+1))
    visited[n] = 0
    return result

result = 0
for i in range(N):
    result = max(result, dfs(i, 1))
    if result >= 5:
        print(1)
        exit()
    i += 1
print(0)