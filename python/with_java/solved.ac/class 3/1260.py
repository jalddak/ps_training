import sys
from collections import deque
input = sys.stdin.readline

def dfs(v, edges, visited, result):
    visited[v] = True
    result.append(v)
    for n in edges[v]:
        if not visited[n]:
            dfs(n, edges, visited, result)

def bfs(v, edges, visited, result):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        result.append(v)
        for n in edges[v]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)

def main():
    n, m, v = map(int, input().split())
    edges = [[] for _ in range(n+1)]

    for _ in range(m):
        s, e = map(int, input().split())
        edges[s].append(e)
        edges[e].append(s)

    edges = list(map(sorted, edges))

    visited = [False for _ in range(n+1)]
    result = []
    dfs(v, edges, visited, result)
    print(" ".join(map(str, result)))

    visited = [False for _ in range(n+1)]
    result = []
    bfs(v, edges, visited, result)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()