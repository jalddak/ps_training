import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n+1)]
edges_reverse = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges_reverse[e].append(s)

S, T = map(int, input().split())

def dfs(start, edges, visited):
    visited[start] = True
    stack = [start]
    while stack:
        now = stack.pop()
        for next in edges[now]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)

fromS = [False for _ in range(n+1)]
fromS[T] = True
dfs(S, edges, fromS)
toT = [False for _ in range(n+1)]
dfs(T, edges_reverse, toT)

fromT = [False for _ in range(n+1)]
fromT[S] = True
dfs(T, edges, fromT)
toS = [False for _ in range(n+1)]
dfs(S, edges_reverse, toS)

result = 0
for i in range(1, n+1):
    if i == S or i == T:
        continue
    if fromS[i] and toT[i] and fromT[i] and toS[i]:
        result += 1

print(result)